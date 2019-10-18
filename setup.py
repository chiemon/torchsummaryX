from setuptools import setup, find_packages

setup(
    name             = "torchsummaryX",
    version          = "1.2.0",
    description      = "Fork from https://github.com/nmhkahn/torchsummaryX.",
    author           = "Chiemon",
    author_email     = "ahxieqi@163.com",
    url              = "https://github.com/chiemon/torchsummaryX",
    packages         =["torchsummaryX"],
    install_requires = ["torch", "numpy", "pandas"],
)
