from setuptools import find_packages, setup

with open("requirements.txt") as f:
    content = f.readlines()
requirements = [x.strip() for x in content if "git+" not in x]

setup(name='ai_weeder_package',
      version="0.2.0",
      description="Plant Identification Model (api_pred)",
      #license="",
      author="AI Weeder Group",
      #author_email="",
      #url="https://github.com/dorwein/ai_weeder",
      install_requires=requirements,
      packages=find_packages(),
      #test_suite="tests",
      #include_package_data: to install data from MANIFEST.in
      include_package_data=True,
      zip_safe=False)
