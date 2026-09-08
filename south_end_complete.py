import marimo

__generated_with = "0.19.8"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(r"""
    # South End Vega-Altair
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    # Keyboard shortcuts
    Most important:
    * <kbd>⌃ Ctrl</kbd>/<kbd>⌘ Cmd</kbd> + <kbd>⇧ Shift</kbd> + <kbd>H</kbd> shows the shortcuts menu
    * <kbd>⌃ Ctrl</kbd>/<kbd>⌘ Cmd</kbd> + <kbd>K</kbd> opens the command palette

    Running cells:
    * <kbd>⌃ Ctrl</kbd>/<kbd>⌘ Cmd</kbd> + <kbd>⏎ Enter</kbd> runs the cell.
    * <kbd>⇧ Shift</kbd> + <kbd>⏎ Enter</kbd> runs the cell and creates a new cell below
    * <kbd>⌃ Ctrl</kbd>/<kbd>⌘ Cmd</kbd> + <kbd>⇧ Shift</kbd> + <kbd>⏎ Enter</kbd> runs the cell and creates a new cell above

    Display:
    * <kbd>⌃ Ctrl</kbd>/<kbd>⌘ Cmd</kbd> + <kbd>B</kbd> formats the cell
    * <kbd>⌃ Ctrl</kbd>/<kbd>⌘ Cmd</kbd> + <kbd>H</kbd> hides cell code
    * <kbd>⌃ Ctrl</kbd>/<kbd>⌘ Cmd</kbd> + <kbd>⇧ Shift</kbd> + <kbd>M</kbd> views a cell as Markdown

    System:
    * <kbd>⌃ Ctrl</kbd>/<kbd>⌘ Cmd</kbd> + <kbd>I</kbd> stops execution
    * <kbd>⌃ Ctrl</kbd>/<kbd>⌘ Cmd</kbd> + <kbd>.</kbd> toggles app view
    * <kbd>⌃ Ctrl</kbd> + <kbd>S</kbd> saves

    Command mode creation & navigation:
    * <kbd>Esc</kbd> in a cell enters command mode
    * <kbd>↑</kbd>/<kbd>↓</kbd> navigate cells; <kbd>⇧ Shift</kbd> + <kbd>↑</kbd>/<kbd>↓</kbd> multi-selects
    * <kbd>A</kbd>/<kbd>B</kbd> creates a cell before/after
    * <kbd>C</kbd>/<kbd>V</kbd> copies/pastes a cell

    Edit mode creation & navigation:
    * <kbd>Enter</kbd> returns to editing
    * <kbd>⌃ Ctrl</kbd>/<kbd>⌘ Cmd</kbd> + <kbd>⇧ Shift</kbd> + <kbd>O</kbd>/<kbd>P</kbd> creates a new cell above/below
    * <kbd>⌃ Ctrl</kbd>/<kbd>⌘ Cmd</kbd> + <kbd>⇧ Shift</kbd> + <kbd>J</kbd>/<kbd>K</kbd> goes to the next/previous cell
    * <kbd>⇧ Shift</kbd> + <kbd>⌫ Backspace</kbd> deletes a cell

    Warning: Some keyboard shortcuts may conflict with browser or OS shortcuts.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    # Background
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    The census tract for the South End begins just on the SE side of Columbus Avenue, as shown in this map:

    ![Map of the South End](public/south_end_map.png)

    Let's explore the demographics of the South End.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    # Setup
    """)
    return


@app.cell
def _():
    import altair as alt
    import marimo as mo
    import pandas as pd
    from altair import datum

    print("Altair version: " + alt.__version__)
    return alt, datum, mo, pd


@app.cell
def _(mo):
    mo.md(r"""
    # Loading Data
    """)
    return


@app.cell
def _(pd):
    df = pd.read_csv("south_end.csv")
    df
    return (df,)


@app.cell
def _(df):
    df[["Category", "Subcategory"]]
    return


@app.cell
def _(df):
    df[["Category", "Subcategory"]].drop_duplicates()
    return


@app.cell
def _(mo):
    mo.md(r"""
    # Creating Visualizations
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Age Distribution by Decade
    """)
    return


@app.cell
def _(alt, df):
    alt.Chart(df).mark_bar().encode(x="Decade:O")
    return


@app.cell
def _(alt, df):
    alt.Chart(df).mark_bar().encode(x="Decade:O", y="Count:Q")
    return


@app.cell
def _(alt, df):
    alt.Chart(df).mark_bar().encode(x="Decade:O", y="Count:Q", color="Subcategory:N")
    return


@app.cell
def _(alt, datum, df):
    alt.Chart(df).mark_bar().encode(
        x="Decade:O", y="Count:Q", color="Subcategory:N"
    ).transform_filter(datum["Category"] == "Age")
    return


@app.cell
def _(alt, df):
    _df = df[df["Category"] == "Age"]
    alt.Chart(_df).mark_bar().encode(x="Decade:O", y="Count:Q", color="Subcategory:N")
    return


@app.cell
def _(alt, datum, df):
    alt.Chart(df).mark_bar().encode(
        x="Decade:O", y="Count:Q", color="Subcategory:N"
    ).transform_filter(datum["Category"] == "Age").properties(
        title="Age Distribution by Decade"
    )
    return


@app.cell
def _(alt, datum, df):
    alt.Chart(df).mark_bar().encode(
        x="Decade:O", y="Count:Q", color=alt.Color("Subcategory:N", title="Age Range")
    ).transform_filter(datum["Category"] == "Age").properties(
        title="Age Distribution by Decade"
    )
    return


@app.cell
def _(alt, datum, df):
    alt.Chart(df).mark_bar().encode(
        x="Decade:O",
        y="Count:Q",
        color=alt.Color("Subcategory:N", title="Age Range", sort="descending"),
        order=alt.Order("Subcategory:N", sort="ascending"),
    ).transform_filter(datum["Category"] == "Age").properties(
        title="Age Distribution by Decade"
    )
    return


@app.cell
def _(alt, datum, df):
    alt.Chart(df).mark_line().encode(
        x="Decade:O",
        y="Count:Q",
        color=alt.Color("Subcategory:N", title="Age Range", sort="descending"),
        order=alt.Order("Subcategory:N", sort="ascending"),
    ).transform_filter(datum["Category"] == "Age").properties(
        title="Age Distribution by Decade"
    )
    return


@app.cell
def _(alt, datum, df):
    alt.Chart(df).mark_area().encode(
        x="Decade:O",
        y="Count:Q",
        color=alt.Color("Subcategory:N", title="Age Range", sort="descending"),
        order=alt.Order("Subcategory:N", sort="ascending"),
    ).transform_filter(datum["Category"] == "Age").properties(
        title="Age Distribution by Decade"
    )
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Educational Attainment by Decade
    """)
    return


@app.cell
def _():
    eduField = "Educational Attainment (age 25+)"
    return (eduField,)


@app.cell
def _(alt, datum, df, eduField):
    alt.Chart(df).mark_bar().encode(
        x="Decade:O",
        y="Count:Q",
        color=alt.Color("Subcategory:N", title=eduField, sort="descending"),
        order=alt.Order("Subcategory:N", sort="descending"),
    ).transform_filter(datum["Category"] == eduField).properties(
        title="Educational Attainment Distribution by Decade"
    )
    return


@app.cell
def _():
    eduSortOrder = [
        "Bachelor's Degree or Higher",
        "Some College or Associate's Degree",
        "High School or GED",
        "less than High School",
    ]
    return (eduSortOrder,)


@app.cell
def _(alt, datum, df, eduField, eduSortOrder):
    alt.Chart(df).mark_bar().encode(
        x="Decade:O",
        y="Count:Q",
        color=alt.Color("Subcategory:N", title=eduField, sort=eduSortOrder),
    ).transform_filter(datum["Category"] == eduField).properties(
        title="Educational Attainment Distribution by Decade"
    )
    return


@app.cell
def _(alt, datum, df, eduField, eduSortOrder):
    alt.Chart(df).mark_bar().encode(
        x="Decade:O",
        y="Count:Q",
        color=alt.Color("Subcategory:N", title=eduField, sort=eduSortOrder),
        order=alt.Order("eduOrdering:N", sort="ascending"),
    ).transform_filter(datum["Category"] == eduField).transform_calculate(
        eduOrdering="0"
        # Altair tries to sort by the eduOrdering field. Since every row has the same value ('0'), there's no meaningful differentiation to sort on. When all items have equal sort keys, Altair falls back to using the natural order of the data.
    ).properties(
        title="Educational Attainment Distribution by Decade"
    )
    return


@app.cell
def _(alt, datum, df, eduField, eduSortOrder):
    alt.Chart(df).mark_bar().encode(
        x="Decade:O",
        y="Count:Q",
        color=alt.Color("Subcategory:N", title=eduField, sort=eduSortOrder),
        column=alt.Column("Subcategory:N", title=eduField, sort=eduSortOrder),
    ).transform_filter(datum["Category"] == eduField).properties(
        title="Educational Attainment Distribution by Decade"
    )
    return


@app.cell
def _(alt, datum, df, eduField, eduSortOrder):
    alt.Chart(df).mark_bar().encode(
        x="Decade:O",
        y="Count:Q",
        color=alt.Color("Subcategory:N", title=eduField, sort=eduSortOrder),
        column=alt.Column(
            "Subcategory:N", title=eduField, sort=eduSortOrder[::-1]
        ),  # ::-1 makes a copy in reverse order
    ).transform_filter(datum["Category"] == eduField).properties(
        title="Educational Attainment Distribution by Decade"
    )
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Race by Decade
    """)
    return


@app.cell
def _(alt, datum, df):
    alt.Chart(df).mark_bar().encode(
        x="Decade:O",
        y="Count:Q",
        color=alt.Color("Subcategory:N", title="Race"),
    ).transform_filter(datum["Category"] == "Race/ Ethnicity").properties(
        title="Race Distribution by Decade"
    )
    return


@app.cell
def _(alt, datum, df):
    chart_race = (
        alt.Chart(df)
        .mark_bar()
        .encode(
            x="Decade:O",
            y="Count:Q",
            color=alt.Color("Subcategory:N", title="Race"),
        )
        .transform_filter(datum["Category"] == "Race/ Ethnicity")
        .properties(title="Race Distribution by Decade")
    )
    chart_race
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Types of Occupancy by Decade
    """)
    return


@app.cell
def _(alt, datum, df):
    alt.Chart(df).mark_bar().encode(
        x="Decade:O",
        y=alt.Y("Count:Q", stack="normalize", title="Occupancy Split"),
        color=alt.Color("Subcategory:N", title="Type of Occupancy"),
    ).transform_filter(
        (datum["Category"] == "Housing Tenure")
        & (datum["Subcategory"] != "Occupied Housing Units")
    ).properties(
        title="Types of Occupancy Distribution by Decade"
    )
    return


@app.cell
def _(alt, datum, df):
    chart_occupancy = (
        alt.Chart(df)
        .mark_bar()
        .encode(
            x="Decade:O",
            y=alt.Y("Count:Q", stack="normalize", title="Occupancy Split"),
            color=alt.Color("Subcategory:N", title="Type of Occupancy"),
        )
        .transform_filter(
            (datum["Category"] == "Housing Tenure")
            & (datum["Subcategory"] != "Occupied Housing Units")
        )
        .properties(title="Types of Occupancy Distribution by Decade")
    )
    chart_occupancy
    return (chart_occupancy,)


@app.cell
def _(mo):
    mo.md(r"""
    # Saving Your Results
    """)
    return


@app.cell
def _(chart_occupancy):
    chart_occupancy.save("charts/chart_occupancy.svg")
    chart_occupancy.save("charts/chart_occupancy.png", scale_factor=3)  # 1-5
    chart_occupancy.save(
        "charts/chart_occupancy.html", embed_options={"renderer": "svg"}
    )
    return


@app.cell
def _(mo):
    mo.md(r"""
    Or use the chart UI:

    ![Screenshot of the vega-altair chart save ui](public\vega-altair-save-ui.png)
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    # Creating Your Infographic

    **Note:** You do not need to do the following steps yourself. The instructor will simply demonstrate what is possible.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## The Pre-2023 and Still Useful way
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's save the chart from above using the ... menu at the top-right in several different formats.

    Here is an example infographic you could create by exporting an SVG and editing in Inkscape or Illustrator:

    ![South End Occupancy Infographic](public/south_end_occupancy_infographic.png)

    In Inkscape:
    * Open the SVG.
    * Use the select tool to select the owner series & the legend with `shift+click`, after first `double-clicking` a lot to get through the groups.
    * Go to Object->Fill and Stroke and pick a gray color.
    * Add the `apartment_building.svg` and scale to ~20% using Object->Transform->Scale
    * Select and edit the text at the top to "Decreasing Renter-Occupied South End Dwellings"
    * File->Save As->Inkscape SVG

    In Illustrator:
    * Open the SVG.
    * Use the magic wand tool to select the owner series & the legend.
    * Edit->Edit Colors->Saturate and reduce saturation.
    * Add the `apartment_building.svg` and scale to ~20% using Object->Transform->Scale
    * Select and edit the text at the top to "Decreasing Renter-Occupied South End Dwellings"
    * File->Export As->SVG
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## A Whole New Exciting Way
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Enter a prompt like this into your favorite AI tool and attach the chart file.

    > This chart shows owner-occupied vs. renter-occupied housing units in the South End of Boston across the decades. Turn this into an informative infographic about how there is an increase in owner-occupied housing units over time. Create it in the style of Dr. Seuss.
    """)
    return


@app.cell
def _(mo):
    _out = None
    with open("public/occupancy_infographic_claude.html", "r", encoding="utf-8") as f:
        _out = mo.iframe(f.read())
    _out
    return


@app.cell(hide_code=True)
def _(mo):
    mo.image("public/occupancy_infographic_gemini.jpg")
    return


if __name__ == "__main__":
    app.run()
