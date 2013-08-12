"""
Tests for creating project registrations.
"""

# Project imports
import base


class RegistrationTests(base.ProjectSmokeTest):

    def test_create_open_ended_registration(self):
        """ Create an Open-Ended Registration. """
        
        registration_url = self.create_registration('Open-Ended Registration')

        self.assertIn(
            'This node is a registration of',
            self.get_element('span.label.label-important').text,
        )

    def test_create_osf_standard_registration(self):
        """ Create an OSF Standard registration """
        registration_url = self.create_registration(
            'OSF-Standard Pre-Data Collection Registration'
        )

        self.assertIn(
            'This node is a registration of',
            self.get_element('span.label.label-important').text
        )