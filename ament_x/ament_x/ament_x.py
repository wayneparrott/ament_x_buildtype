from ros2pkg.api.build_type import BaseBuildType
from ros2pkg.api.create import create_file
from ros2pkg.api.create import create_folder

class AmentXBuildType(BaseBuildType):

    def __init__(self):
        super(AmentXBuildType, self).__init__()

    def populate(self):
      super(AmentXBuildType, self).populate()

      params = {
        'package_name': self.package.name
      }
      create_file(
        'ament_x',
        'ament_x/main.x.em',
        self.source_directory,
        'main.x',
        params)

    def create_source_folders(self):
      super(AmentXBuildType, self).create_source_folders()

      print('creating source folder')
      self.source_directory = create_folder('src', self.package_directory)
      if not self.source_directory:
        return 'unable to create source folder in ' + self.package_directory
