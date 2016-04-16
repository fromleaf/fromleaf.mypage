from fromleaf_common.tests import UserTestCase
from fromleaf_opening.tests import OpeningPageTestCase
from fromleaf_aboutme.tests import AboutMePageTestCase
from fromleaf_myskill.tests import MySkillPageTestCase
from fromleaf_career.tests import CareerPageTestCase

# Test User 
test_user = UserTestCase()
test_user.insert_user_info()

# Test Opening Page
test_opening_page = OpeningPageTestCase()
test_opening_page.insert_opening_page_info()

# Test AboutMe Page
test_aboutme_page = AboutMePageTestCase()
test_aboutme_page.insert_aboutme_page_info()


# Test MySkill Page
test_myskill_page = MySkillPageTestCase()
test_myskill_page.insert_myskill_page_info()

# Test Career Page
test_career_page = CareerPageTestCase()
test_career_page.insert_career_page_all()