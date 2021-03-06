"""arturo-stac-api."""

from setuptools import find_packages, setup

with open("README.md") as f:
    desc = f.read()


install_requires = [
    "attrs",
    "uvicorn[standard]",
    "gunicorn",
    "fastapi>=0.60.0",
    "alembic",
    "psycopg2-binary",
    "shapely",
    "sqlalchemy",
    "geoalchemy2<0.8.0",
    "sqlakeyset",
    "stac-pydantic>=1.3.5",
    "pydantic[dotenv]",
    "titiler==0.1.0a12",
    "fastapi-utils",
]

extra_reqs = {
    "dev": ["pytest", "pytest-cov", "pytest-asyncio", "pre-commit", "requests"],
    "docs": ["mkdocs", "mkdocs-material"],
}


setup(
    name="arturo-stac-api",
    description="Arturo's STAC compliant API implementation",
    long_description=desc,
    long_description_content_type="text/markdown",
    version="1.1.0",
    python_requires=">=3.8",
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
    ],
    keywords="STAC FastAPI COG",
    author=u"Arturo Engineering",
    author_email="engineering@arturo.ai",
    url="https://github.com/arturo-ai/arturo-stac-api",
    license="MIT",
    packages=find_packages(exclude=["alembic", "tests", "scripts"]),
    zip_safe=False,
    install_requires=install_requires,
    tests_require=extra_reqs["dev"],
    extras_require=extra_reqs,
)
