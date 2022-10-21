from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="mkdocs-git-timeline-plugin",
    version="0.0.2",
    description="Mkdocs plugin to display git timeline of a page",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="mkdocs git timeline contributors committers authors plugin",
    url="https://github.com/timvink/mkdocs-git-timeline-plugin",
    author="Tim Vink, Franciszek Piszcz",
    author_email="vinktim@gmail.com, franek.piszcz@gmail.com",
    license="MIT",
    python_requires=">=3.6",
    classifiers=[
        "Operating System :: OS Independent",
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3 :: Only',
        "License :: OSI Approved :: MIT License",
        'Topic :: Documentation',
        'Topic :: Text Processing',
    ],
    install_requires=["mkdocs>=1.0"],
    packages=find_packages(),
    entry_points={
        "mkdocs.plugins": [
            "git-timeline = mkdocs_git_timeline_plugin.plugin:GitTimelinePlugin"
        ]
    },
)
