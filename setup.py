from setuptools import find_packages, setup
setup(
    name = 'mcqgnerator',
    version = '0.0.1',
    author = 'sushmitha',
    author_email = 'sushmithalakshmi1010@gmail.com',    
    install_requirements = ["openai", "langchain", "streamlit", "python-dotenv", "PyPDF2" ], 
    packages = find_packages()
)