# COMPATIBILITY ISSUES:
# Plotly's px.scatter function uses statsmodels for lowess trendlines under the hood.
# Which won't work when hosting on GitHub Pages, so we'll comment it out.

# IMPORT the packages we need (or might want to use) first.
# NOTE: Each package should be added to requirements.txt,
#       so the packages can be INSTALLED into the project virtual environment.

import faicons as fa  # For using font awesome in cards
import pandas as pd  # Pandas for data manipulation, required by plotly.express
import plotly.express as px  # Plotly Express for making Plotly plots
from shinywidgets import render_plotly  # For rendering Plotly plots
from shiny import reactive, render, req  # To define reactive calculations
from shiny.express import input, ui  # To define the user interface

# ALWAYS familiarize yourself with the data you are working with first.
# Column names for the tips dataset include:
# - total_bill: the bill amount (dollars)
# - tip: the tip amount (dollars)
# - sex: Male or Female
# - smoker: Yes or No
# - day: Day of the week
# - time: Lunch or Dinner
# - size: Size of the party

# Load data into a pandas DataFrame
# Use the tips dataset from Plotly Express
tips_df = px.data.tips()

# Compute static values
bill_range_tuple = (min(tips_df.total_bill), max(tips_df.total_bill))

# Define the Shiny UI Page layout
# Call the ui.page_opts() function to set the page title and make the page fillable
ui.page_opts(title="PyShiny Express: Restaurant Tipping Example", fillable=True)

# Add a Shiny UI sidebar for user interaction
# Use the ui.sidebar() function to create a sidebar
# Set the open parameter to "open" to make the sidebar open by default
# Use a with block to add content to the sidebar
# Using Shiny Express there are no punctuation between ui elements
# Use the ui.h2() function to add a 2nd level header to the sidebar
#   pass in a string argument (in quotes) to set the header text
# Use the ui.input_slider() function to add a slider to the sidebar
#   pass in a string argument (in quotes) to set the input label
#   pass in a string argument (in quotes) to set the input label
#   pass in a tuple argument to set the minimum and maximum values
#   pass in a string argument (in quotes) to set the prefix
# Use the ui.input_checkbox_group() function to add a checkbox group to the sidebar
#   pass in a string argument (in quotes) to set the input label
#   pass in a list argument to set the input options
#   pass in a list argument to set the selected options
#   pass in a boolean argument to set the inline option
# Use the ui.input_action_button() function to add an action button to the sidebar
#   pass in a string argument (in quotes) to set the button label
# Use the ui.hr() function to add a horizontal rule to the sidebar
# Use the ui.h6() function to add a 6th level header to the sidebar
#   pass in a string argument (in quotes) to set the header text
# Use ui.a() to add a hyperlink to the sidebar
#   pass in two arguments:
#   the text for the hyperlink (in quotes)
#   the URL for the hyperlink (in quotes)
#   set the target parameter to "_blank" to open the link in a new tab
# When passing in multiple arguments to a function, separate them with commas.

with ui.sidebar(open="open"):

    ui.h2("Sidebar")

    ui.input_slider(
        "selected_range_total_bill",
        "Bill amount",
        min=bill_range_tuple[0],
        max=bill_range_tuple[1],
        value=bill_range_tuple,
        pre="$",
    )

    ui.input_checkbox_group(
        "selected_time_category",
        "Food service",
        ["Lunch", "Dinner"],
        selected=["Lunch", "Dinner"],
        inline=True,
    )

    ui.input_action_button("reset_event", "Reset filter")
    ui.hr()
    ui.h6("Links:")
    ui.a(
        "GitHub Source",
        href="https://github.com/denisecase/pyshiny-tips-dashboard-express",
        target="_blank",
    )
    ui.a(
        "GitHub App",
        href="https://denisecase.github.io/pyshiny-tips-dashboard-express/",
        target="_blank",
    )
    ui.a("PyShiny", href="https://shiny.posit.co/py/", target="_blank")
    ui.a(
        "PyShiny Express",
        href="hhttps://shiny.posit.co/blog/posts/shiny-express/",
        target="_blank",
    )
    ui.a(
        "See the Code",
        href="https://shiny.posit.co/py/docs/user-interfaces.html#all-together-now",
        target="_blank",
    )

# Add main content
ICONS = {
    "user": fa.icon_svg("user", "regular"),
    "wallet": fa.icon_svg("wallet"),
    "currency-dollar": fa.icon_svg("dollar-sign"),
    "gear": fa.icon_svg("gear"),
}

# Value boxes
with ui.layout_columns(fill=False):

    with ui.value_box(showcase=ICONS["user"]):
        "Total tippers"

        @render.express
        def total_tippers():
            filtered_data().shape[0]

    with ui.value_box(showcase=ICONS["wallet"]):
        "Average tip"

        @render.express
        def average_tip():
            d = filtered_data()
            if d.shape[0] > 0:
                perc = d.tip / d.total_bill
                f"{perc.mean():.1%}"

    with ui.value_box(showcase=ICONS["currency-dollar"]):
        "Average bill"

        @render.express
        def average_bill():
            d = filtered_data()
            if d.shape[0] > 0:
                bill = d.total_bill.mean()
                f"${bill:.2f}"


# Tables and charts
with ui.layout_columns(col_widths=[6, 6, 12]):

    with ui.card(full_screen=True):
        ui.card_header("Tips data")

        @render.data_frame
        def table():
            return render.DataGrid(filtered_data())

    with ui.card(full_screen=True):
        with ui.card_header(class_="d-flex justify-content-between align-items-center"):
            "Total bill vs tip"
            with ui.popover(title="Add a color variable", placement="top"):
                ICONS["gear"]
                ui.input_radio_buttons(
                    "scatter_color",
                    None,
                    ["none", "sex", "smoker", "day", "time"],
                    inline=True,
                )

        @render_plotly
        def scatterplot():
            color = input.scatter_color()
            return px.scatter(
                filtered_data(),
                x="total_bill",
                y="tip",
                color=None if color == "none" else color,
                # trendline="lowess"
            )

    with ui.card(full_screen=True):
        with ui.card_header(class_="d-flex justify-content-between align-items-center"):
            "Tip percentages"
            with ui.popover(title="Add a color variable"):
                ICONS["gear"]
                ui.input_radio_buttons(
                    "tip_perc_y",
                    "Split by:",
                    ["sex", "smoker", "day", "time"],
                    selected="day",
                    inline=True,
                )

        @render_plotly
        def tip_perc():
            filtered_df = filtered_data()
            filtered_df["percent"] = filtered_df.tip / filtered_df.total_bill
            yvar = input.tip_perc_y()

            # Create a violin plot with Plotly
            violin_figure = px.violin(
                filtered_df,
                y="percent",
                color=yvar,  # This will split the violin plot by the selected variable
                box=True,  # Displays a box plot inside the violin
                points="all",  # Shows all points
                hover_data=tips_df.columns,  # Adds all other data as hover information
                title="Distribution of Tip Percentages by " + yvar.capitalize(),
            )

            # Update layout for better readability
            violin_figure.update_layout(
                yaxis_title="Tip Percentage",
                legend_title=yvar.capitalize(),
                legend=dict(
                    orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1
                ),
            )
            return violin_figure


# --------------------------------------------------------
# Reactive calculations and effects
# --------------------------------------------------------

# Add a reactive calculation to filter the data
# By decorating the function with @reactive, we can use the function to filter the data
# The function will be called whenever an input functions used to generate that output changes.
# Any output that depends on filtered_data() will be updated when the data changes.

# In this case, notice that many outputs depend on filtered_data().


@reactive.calc
def filtered_data():

    # Get the selected range from the input as a tuple (min, max)
    selected_tuple = input.selected_range_total_bill()

    # Use the between() method to filter the DataFrame
    # The method returns a boolean Series with the same index as the original DataFrame
    # Each row is:
    #   True if the total bill is in the input.selected_range_total_bill()
    #   False if the total bill is not
    isTotalBillInRange = tips_df.total_bill.between(
        selected_tuple[0], selected_tuple[1]
    )

    # Use the isin() method to filter the DataFrame
    # The method returns a boolean Series with the same index as the original DataFrame
    # Each row is:
    #   True if the row is in the input.selected_species() list
    #   False if the species is not
    isInSelectedTime = tips_df.time.isin(input.selected_time_category())

    # Use the boolean filter mask in square brackets to filter the DataFrame
    # Return the filtered DataFrame when the function is triggered
    # Filter masks can be combined with the & operator for AND and the | operator for OR
    return tips_df[isTotalBillInRange & isInSelectedTime]


@reactive.effect
@reactive.event(input.reset_event)
def _():
    ui.update_slider("selected_range_total_bill", value=bill_range_tuple)

    ui.update_checkbox_group("selected_time_category", selected=["Lunch", "Dinner"])


# Additional Python Notes
# ------------------------
# Capitalization matters in Python. Python is case-sensitive: min and Min are different.
# Spelling matters in Python. You must match the spelling of functions and variables exactly.
# Indentation matters in Python. Indentation is used to define code blocks and must be consistent.

# Functions
# ---------
# Functions are used to group code together and make it more readable and reusable.
# We define custom functions that can be called later in the code.
# Functions are blocks of logic that can take inputs, perform work, and return outputs.

# Defining Functions
# ------------------
# Define a function using the def keyword, followed by the function name, parentheses, and a colon. 
# The function name should describe what the function does.
# In the parentheses, specify the inputs needed as arguments the function takes.
# For example:
#    The function filtered_data() takes no arguments.
#    The function between(min, max) takes two arguments, a minimum and maximum value.
#    Arguments can be positional or keyword arguments, labeled with a parameter name.

# The function body is indented (consistently!) after the colon. 
# Use the return keyword to return a value from a function.
    
# Calling Functions
# -----------------
# Call a function by using its name followed by parentheses and any required arguments.
    
# Decorators
# ----------
# Use the @ symbol to decorate a function with a decorator.
# Decorators a concise way of calling a function on a function.
# We don't typically write decorators, but we often use them.
    