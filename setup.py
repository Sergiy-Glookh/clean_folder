from setuptools import setup, find_namespace_packages

setup(name='clean-folder',
      version='0.0.1',
      description='recursively sorting files in a specified folder based on their extensions and normalizing file names',
      url='https://github.com/Sergiy-Glookh/clean_folder',
      author='Sregiy Glookh',
      author_email='sglookh@gmail.com',
      license='MIT',
      packages=find_namespace_packages(),
      include_package_data=True,
      install_requires=['py7zr'],
      entry_points={'console_scripts': ['clean-folder = clean_folder.clean_folder.clean:disassemble_junk']}
      )

