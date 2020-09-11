import requests


class RegistryMixin:

    def check_registry(self):
        print("(3/5) registry")
        results = [
            self.has_bintray_badge(),
            self.has_conda_badge(),
            self.has_cran_badge(),
            self.has_pypi_badge(),
            self.has_rsd_badge(),
            self.is_on_github_marketplace()
        ]
        return True in results

    def has_bintray_badge(self):
        regexes = [r"https://api\.bintray\.com/packages/.*/.*/.*/images/download\.svg"]
        return self._eval_regexes(regexes)

    def has_conda_badge(self):
        regexes = [r"https://anaconda\.org/.*/.*/badges/installer/conda\.svg"]
        return self._eval_regexes(regexes)

    def has_cran_badge(self):
        regexes = [r"https://cranlogs\.r-pkg\.org/badges/.*",
                   r"https://cranlogs\.r-pkg\.org/badges/grand-total/.*"]
        return self._eval_regexes(regexes)

    def has_pypi_badge(self):
        regexes = [r"https://img\.shields\.io/pypi/v/[^.]*",
                   r"https://pypi\.python\.org/pypi/",
                   r"https://badge\.fury\.io/py/.*\.svg"]
        return self._eval_regexes(regexes)

    def has_rsd_badge(self):
        regexes = [r"https://img\.shields\.io/badge/RSD-.*",
                   r"https://img\.shields\.io/badge/rsd-.*"]
        return self._eval_regexes(regexes)

    def is_on_github_marketplace(self):
        try:
            response = requests.get(self.url)
            # If the response was successful, no Exception will be raised
            response.raise_for_status()
        except requests.HTTPError:
            self.print_state(check_name="is_on_github_marketplace", state=False)
            return False

        html = response.text
        r = "Use this GitHub Action with your project" in html and \
            "Add this Action to an existing workflow or create a new one." in html
        self.print_state(check_name="is_on_github_marketplace", state=r)
        return r
