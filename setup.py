"""Install setup."""
import setuptools

setuptools.setup(
    name="haberman",
    version="0.0.1",
    url="git@github.com:ScottSnapperLab/Ileal_Tx_CD_Haberman_2014.git",

    author="Gus Dunn",
    author_email="w.gus.dunn@gmail.com",

    description="A re-analysis using the VIPER pipeline from Dana Farber.",
    # long_description=open('README.rst').read(),

    packages=setuptools.find_packages('src/python'),


    install_requires=["click",
                      "munch",
                      "seaborn",
                      "pandas",
                      "numexpr",
                      "numpy",
                      "xlrd",
                      "xlwt",
                      ],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
