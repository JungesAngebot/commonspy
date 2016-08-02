from commonspy.configuration import OverwriteableConfiguration

config = OverwriteableConfiguration.create_from_file('config.json')

config.property('database.mongo_host')
