"""
description: 페이지 사용자 정보 및 글 정보를 입력.
"""

from fromleaf_common.tests import UserTestCase
from fromleaf_opening.tests import OpeningPageTestCase
from fromleaf_aboutme.tests import AboutMePageTestCase
from fromleaf_myskill.tests import MySkillPageTestCase
from fromleaf_career.tests import CareerPageTestCase
from fromleaf_playing.tests import PlayingPageTestCase
from fromleaf_contactme.tests import ContactMePageTestCase

# CHECK: 이게 테스트는 아니지 않는가?

# Test User 
test_user = UserTestCase()
test_user.insert_user()

# Test Opening Page
test_opening_page = OpeningPageTestCase()
test_opening_page.insert_opening_page()

# Test AboutMe Page
test_aboutme_page = AboutMePageTestCase()
test_aboutme_page.insert_aboutme_page()

# Test MySkill Page
test_myskill_page = MySkillPageTestCase()
test_myskill_page.insert_myskill_page()

# Test Career Page
test_career_page = CareerPageTestCase()
test_career_page.insert_career_page()

# Test Playing Page
test_playing_page = PlayingPageTestCase()
test_playing_page.insert_playing_page()


# Test ContactMe Page
test_contactme_page = ContactMePageTestCase()
test_contactme_page.insert_contactme_page()
