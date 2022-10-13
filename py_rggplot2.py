# Ref : https://rpy2.github.io/doc/latest/html/introduction.html
# rpy2 in Python for ggplot2 
import rpy2.robjects as ro
import rpy2.robjects.lib.ggplot2 as ggplot2
from rpy2.robjects.packages import importr, data
base = importr('base')
stats = importr('stats')
grdevices = importr('grDevices')
datasets = importr('datasets')
mtcars = data(datasets).fetch('mtcars')['mtcars']

# import rpy2's package module
import rpy2.robjects.packages as rpackages
# import R's utility package
utils = rpackages.importr('utils')
# R vector of strings
from rpy2.robjects.vectors import StrVector
utils.install_packages(StrVector('ggplot2'))

gp = (ggplot2.ggplot(mtcars) + \
     ggplot2.aes_string(x='wt', y='mpg', col='factor(cyl)')) + \
     ggplot2.geom_point()

gp.plot()
grdevices = importr('grDevices')

gp2 = gp + ggplot2.geom_smooth(ggplot2.aes_string(group = 'cyl'),
                               method = 'lm'))
gp2.plot()
grdevices = importr('grDevices')
