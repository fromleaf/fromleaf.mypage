from fromleaf_common.tests import UserTestCase
from fromleaf_opening.tests import OpeningPageTestCase
from fromleaf_aboutme.tests import AboutMePageTestCase


# Test User 
test_user = UserTestCase()
test_user.insert_user_info()

# Test Opening Page
test_opening_page = OpeningPageTestCase()
test_opening_page.insert_opening_page_info()

# Test AboutMe Page
test_aboutme_page = AboutMePageTestCase()
test_aboutme_page.insert_aboutme_page_info()


