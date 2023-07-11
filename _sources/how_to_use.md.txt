# How to use

If you just want to plot all pulsars simply run:

```
filter_and_plot
```

which will look like this:

![filter_and_plot](images/pulsar_plot_all.png)

If you want to do something else you can use `-h` to list your options.

You can filter the sources by their declination with `--dec_min` and `--dec_max`.
For example you can plot all pulsars in the souther hemisphere with:

```
filter_and_plot --dec_max 0
```

![filter_and_plot](images/pulsar_plot_south.png)

You can also filter by source name so if you just wanted to plot your favorite pulsar you could do:

```
filter_and_plot --source_name J1705-1903 J1705-1903
```

![filter_and_plot](images/pulsar_plot_source.png)