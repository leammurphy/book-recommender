def read_item_names(df):
    """Read book title and id from a csv file and return two dictionaries to
    convert raw ids into book titles and book titles into raw ids.
    """
    # Create dictionaries to convert raw ids into book titles and book titles
    # into raw ids
    rid_to_name = {}
    name_to_rid = {}
    for index, row in df.iterrows():
        rid = str(row["book_id"])
        name = row["title"]
        rid_to_name[rid] = name
        name_to_rid[name] = rid

    return rid_to_name, name_to_rid