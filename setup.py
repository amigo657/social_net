import pathlib
from typing import List, TypeVar
from setuptools import setup, find_packages


Self = TypeVar("Self")


class Setup:
    base_dir = pathlib.Path(__file__).parent.absolute()
    lib_dir = "snet"

    def __init__(self) -> None:
        self.version = self.get_version()
        self.long_desc = self.get_readme()
        self.packages = self.get_packages()
        self.license = self.get_license()

    def get_version(self) -> str:
        with open(self.base_dir / "VERSION") as file: 
            return file.readline().strip()

    def get_readme(self) -> str:
        with open(self.base_dir / "README.md") as file:
            return file.read().strip()

    def get_packages(self) -> List[str]:
        with open(self.base_dir / "requirements.txt") as file:
            return [package.strip() for package in file.readlines() if package]

    def get_license(self) -> str:
        with open(self.base_dir / "LICENSE") as file:
            return file.read().strip()

    def add_version(self) -> Self:
        version_line = '__version__ = "{}"\n'.format(self.version)
        init_file_path = self.base_dir / self.lib_dir / "__init__.py"
        try:
            with open(init_file_path) as init_file:
                code = init_file.readlines()
        except FileExistsError:
            code = [version_line]
        else:
            import_position = None
            for index, line in enumerate(code):
                if "__version__" in line:
                    code[index] = version_line
                    break
                if "import" in line:
                    import_position = index
            else:
                if import_position is not None:
                    new_line_pos = import_position + 1
                    code.insert(new_line_pos, version_line)
                    code.insert(new_line_pos, "\n")
                else:
                    code.insert(0, "\n")
                    code.insert(0, version_line)
        with open(init_file_path, "w") as init_file:
            init_file.writelines(code)
        return self

    def install(self, author: str, email: str, url: str):
        setup(
            name=self.lib_dir,
            version=self.version,
            author=author,
            author_email=email,
            url=url,
            packages=find_packages(".", include=[self.lib_dir]),
            package_dir={"": "."},
            include_package_data=True,
            license=self.license,
            description="REST API for social network.",
            long_description=self.long_desc,
            long_description_content_type="text/markdown",
            install_requires=self.packages,
            python_requires=">=3.8",
            zip_safe=False,
            entry_points={"console_scripts": ["snet_run = snet.app:run"]},
            classifiers=[
                "Development Status :: 3 - Alpha"
                if "dev" in self.version
                else "Development Status :: 4 - Beta"
                if "rc" in self.version
                else "Development Status :: 5 - Production/Stable"
            ]
        )


Setup().add_version().install(
    "Kolya Gajdym",
    "amigo.bro.657@gmail.com",
    "https://github.com/amigo657/social_net",
)