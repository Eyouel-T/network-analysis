import os
import sys
import unittest

import pandas as pd

rpath = os.path.abspath('..')
if rpath not in sys.path:
    sys.path.insert(0, rpath)

from src.loader import SlackDataLoader


class SlackDataLoaderTestCase(unittest.TestCase):
    def setUp(self):
        # Set up any necessary dependencies or configurations for the tests
        self.path = "../anonymized"
        self.loader = SlackDataLoader(self.path)

    def tearDown(self):
        # Clean up after each test if necessary
        pass

    def test_get_users_columns(self):
        # Define the expected columns in the DataFrame
        expected_columns = ['id', 'team_id', 'name', 'deleted', 'color', 'real_name', 'tz',
                            'tz_label', 'tz_offset', 'profile', 'is_admin', 'is_owner',
                            'is_primary_owner', 'is_restricted', 'is_ultra_restricted', 'is_bot',
                            'is_app_user', 'updated', 'is_email_confirmed',
                            'who_can_share_contact_card', 'is_invited_user']

        # Call the method to get the messages DataFrame
        messages = self.loader.get_users()
        messages_df = pd.DataFrame(messages)
        # Check if the DataFrame has the expected columns
        self.assertListEqual(list(messages_df.columns), expected_columns)

    def test_get_channels_columns(self):
        # Define the expected columns in the DataFrame
        expected_columns = ['id', 'name', 'created', 'creator', 'is_archived', 'is_general',
                            'members', 'topic', 'purpose', 'pins']

        # Call the method to get the users DataFrame
        users = self.loader.get_channels()
        users_df = pd.DataFrame(users)
        # Check if the DataFrame has the expected columns
        self.assertListEqual(list(users_df.columns), expected_columns)


if __name__ == '__main__':
    unittest.main()
