from __future__ import annotations

from enum import Enum

class Section(Enum):
    """
    This class represents the news sections.
    """
    ANY = "any"
    ARTS = "Arts"
    BOOKS = "Books"
    BUSINESS = "Business"
    MOVIES = "Movies"
    NEW_YORK = "New York"
    OPINION = "Opinion"
    SPORTS = "Sports"
    STYLE = "Style"
    TRAVEL = "Travel"
    U_S = "U.S."
    WORLD = "World"


# <input type="checkbox" data-testid="DropdownLabelCheckbox" value="Arts|nyt://section/6e6ee292-b4bd-5006-a619-9ceab03524f2">
# <input type="checkbox" data-testid="DropdownLabelCheckbox" value="Business|nyt://section/0415b2b0-513a-5e78-80da-21ab770cb753">
#<input type="checkbox" data-testid="DropdownLabelCheckbox" value="Movies|nyt://section/62b3d471-4ae5-5ac2-836f-cb7ad531c4cb">
# <input type="checkbox" data-testid="DropdownLabelCheckbox" value="New York|nyt://section/39480374-66d3-5603-9ce1-58cfa12988e2">
# <input type="checkbox" data-testid="DropdownLabelCheckbox" value="Opinion|nyt://section/d7a71185-aa60-5635-bce0-5fab76c7c297">
# <input type="checkbox" data-testid="DropdownLabelCheckbox" value="Sports|nyt://section/4381411b-670f-5459-8277-b181485a19ec">
# <input type="checkbox" data-testid="DropdownLabelCheckbox" value="Travel|nyt://section/b2fb7c08-4f8e-5cff-8e14-aff8a49a9934">
# <input type="checkbox" data-testid="DropdownLabelCheckbox" value="U.S.|nyt://section/a34d3d6c-c77f-5931-b951-241b4e28681c">
# <input type="checkbox" data-testid="DropdownLabelCheckbox" value="World|nyt://section/70e865b6-cc70-5181-84c9-8368b3a5c34b">
#<input type="checkbox" value="any" checked="">
