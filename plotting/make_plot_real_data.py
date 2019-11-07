#! /usr/bin/env python3

import xarray as xr
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pint
# import numpy as np
# import sys
from pandas.plotting import register_matplotlib_converters
from pathlib import Path
register_matplotlib_converters()

# Read in one netCDF data file. Look at the default vs. optional for
# scalar variables.
if True:
    # ncdump -ht ../data/sgpmetE13.b1/sgpmetE13.b1.20191101.000000.cdf | less
    filename = str(Path('..', 'data', 'sgpmetE13.b1', 'sgpmetE13.b1.20191101.000000.cdf'))
    met_ds = xr.open_mfdataset(filename, combine='nested', concat_dim='time')
#    met_ds = xr.open_mfdataset(filename, combine='nested',
#                               concat_dim='time', data_vars='minimal')

    print(met_ds)
#    print(met_ds.data_vars)
#    print(list(met_ds.data_vars))
#    print(met_ds['atmos_pressure'])
#    print(met_ds['atmos_pressure'].data)
# #   np.set_printoptions(threshold=sys.maxsize)
#    print(type(met_ds['atmos_pressure'].values))
#    print(met_ds['atmos_pressure'].values)
#    print(met_ds['atmos_pressure'].attrs)
#    print(met_ds['atmos_pressure'].attrs['long_name'])
#    print(met_ds['atmos_pressure'].attrs['does_not_exist'])

#    try:
#        print(met_ds['atmos_pressure'].attrs['does_not_exist'])
#    except KeyError:
#        print('\nCaught the error for "{var_name}" and am now executing the print statement'
#              ' under the except.\n'.format(var_name='atmos_pressure'))

# Read in netCDF data file and exclude some variables.
if False:
    drop_vars = ['base_time', 'time_offset', 'vapor_pressure_std', 'wspd_arith_mean',
                 'qc_wspd_arith_mean', 'wspd_vec_mean', 'qc_wspd_vec_mean',
                 'wdir_vec_mean', 'qc_wdir_vec_mean', 'wdir_vec_std', 'tbrg_precip_total',
                 'qc_tbrg_precip_total', 'tbrg_precip_total_corr', 'qc_tbrg_precip_total_corr',
                 'org_precip_rate_mean', 'qc_org_precip_rate_mean', 'pwd_err_code',
                 'pwd_mean_vis_1min', 'qc_pwd_mean_vis_1min', 'pwd_mean_vis_10min',
                 'qc_pwd_mean_vis_10min', 'pwd_pw_code_inst', 'qc_pwd_pw_code_inst',
                 'pwd_pw_code_15min', 'qc_pwd_pw_code_15min', 'pwd_pw_code_1hr',
                 'qc_pwd_pw_code_1hr', 'pwd_precip_rate_mean_1min',
                 'qc_pwd_precip_rate_mean_1min', 'pwd_cumul_rain', 'qc_pwd_cumul_rain',
                 'pwd_cumul_snow', 'qc_pwd_cumul_snow', 'logger_volt', 'qc_logger_volt',
                 'logger_temp', 'qc_logger_temp', 'temp_std', 'rh_mean', 'qc_rh_mean',
                 'rh_std', 'vapor_pressure_mean', 'qc_vapor_pressure_mean']
    filename = str(Path('..', 'data', 'sgpmetE13.b1', 'sgpmetE13.b1.20191101.000000.cdf'))
    met_ds = xr.open_mfdataset(filename, combine='nested', concat_dim='time',
                               data_vars='minimal', drop_variables=drop_vars)

    print(met_ds)

# Read in netCDF data files using command line syntax for regular expression.
if False:
    filename = str(Path('..', 'data', 'sgpmetE13.b1', 'sgpmetE13.b1.*.cdf'))
    met_ds = xr.open_mfdataset(filename, combine='nested', concat_dim='time')

    print(met_ds)

    del met_ds['base_time']
    del met_ds['time_offset']
    del met_ds['atmos_pressure']
    del met_ds['qc_atmos_pressure']

    # Now that we have done somethign to the Xarray object lets write it to disk.
    # When you look at the file notice the number of time samples and missing
    # variables.
    # # ncdump -ht our_written_file.nc | less
    met_ds.to_netcdf(path='our_written_file.nc', mode='w', format='NETCDF4')


if False:
    filename = str(Path('..', 'data', 'sgpmetE13.b1', 'sgpmetE13.b1.20191101.000000.cdf'))
    met_ds = xr.open_mfdataset(filename, combine='nested', concat_dim='time')

    met_ds['temp_mean'].plot()
    plt.show()


#    fig, axes = plt.subplots(nrows=2)
#    met_ds['temp_mean'].plot(ax=axes[0])
#
#    met_ds['rh_mean'].plot(ax=axes[1])
#    plt.show()

if False:
    filename = str(Path('..', 'data', 'sgpceilC1.b1', 'sgpceilC1.b1.20191103.000012.nc'))
    ceil_ds = xr.open_mfdataset(filename, combine='nested', concat_dim='time')

    # Make a plot.
    # Things are not quite what you want!?!?
    # Where do we begin?
    # The plot is actually being made by pclormesh() call.
    ceil_ds['backscatter'].plot()
    plt.show()


# Lets pause with Xarray plotting and start with the true library that is making
# the plot, matplotlib. Once we understand what is going on underneath we can
# make the plots we want with the same/similar calls with Xarray.
if False:
    filename = str(Path('..', 'data', 'sgpmetE13.b1', 'sgpmetE13.b1.20191104.000000.cdf'))
    met_ds = xr.open_mfdataset(filename, combine='nested', concat_dim='time')

    # It will always save you time in the future if you can reduce the number
    # of hardcoded values in the code. This seems like extra work but it will
    # save you loads of time later on.
    var_name = 'temp_mean'
    var_name2 = 'rh_mean'

    # ---- (4) ---- #
    if False:
        # Convert the units of the data
        desired_temp_unit = 'degF'  # The correct term matters. Follow UDUNITS.
        ureg = pint.UnitRegistry()  # Set up the regestry object.
        data = met_ds[var_name].values  # Get the data from Xarray object.

        # Now we use the units registry with the units in the Xarray objct
        # to tell Pint what units is the data in.
        xarry_units = met_ds[var_name].attrs['units']
        data = data * ureg[xarry_units]

        # Remember the data is in "Pint" space now, not Numpy only space. That means
        # the data may not work with the regular numpy or matplotlib functions?
        print('\ndata.magnitude:', data.magnitude)
        print('data.units:', data.units)

        # Here we use a Pint method to change the units from degC to degF.
        data = data.to(ureg[desired_temp_unit])
        print('\ndata:', data)
        print()

        # We changed the data but we have not put it back into the Xarray object yet.
        met_ds[var_name].values = data.magnitude

        # We changed the units but we need to update the attribute in the Xarray object
        # or else we will be very confused when we go to use the data.
        met_ds[var_name].attrs['units'] = desired_temp_unit

        # Deleting the temporary data variable is not necessary but it does save space (not
        # really necessary) and stops us from using it incorrectly later.
        del data

    # Create the figure (the blank white space) and the axes (the box where plotted
    # data goes and set variabls to call later.
    fig, axes = plt.subplots()

    # Now make the plot by extracting the time and data from object.
    # matplotlib is smart enough to extract what it needs if you pass it the dataarray
    # instead of a numpy array.
    line1_color = 'blue'
    line1 = axes.plot(met_ds['time'], met_ds[var_name], label='Temperature', color=line1_color)

    # Format the x-axis to show hour and minutes only.
    # ---- (1) ---- #
    if False:
        myFmt = mdates.DateFormatter('%H:%M')
        axes.xaxis.set_major_formatter(myFmt)

    # ---- (2) ---- #
    # Plot one full day not the time range of the data.
    # Get the first time value from the object
    if False:
        first_time = met_ds['time'].values[0]

        # Change the precision of the time value from sub-second to day.
        # Then add one to that value to set the end of the range value.
        xrng = [first_time.astype('datetime64[D]'),
                first_time.astype('datetime64[D]') + 1]
        print(xrng)
        axes.set_xlim(xrng)  # Set the xrange for plot window

    # ---- (3) ---- #
    # Now lets be a real scientist and add some axis labels
    if False:
        y_label = met_ds[var_name].attrs['long_name']
        y_label = y_label + ' (' + met_ds[var_name].attrs['units'] + ')'
        axes.set_ylabel(y_label, color=line1_color)

        # Set the x-axis label
        axes.set_xlabel('Time (UTC)')

    # ---- (5) ---- #
    # But when you plot temperature you typically want to plot RH next.
    # How about on the same plot? (Wow mind blown!)
    if False:
        axes_right = axes.twinx()  # Create a new y-axis but share same x-axis.
        line2_color = 'red'
        # Plot the RH data on the new right axis, using the line2_color.
        line2 = axes_right.plot(met_ds['time'], met_ds[var_name2], color=line2_color, label='RH')

#        axes.legend()

    # ---- if time ---- #
    # But why is the RH line not in the legend? This is a bit complicated so if
    # you want to ignore that's fine.
#    if False:
#        # Add the two lines objects to same list. line1 and line2 are single element lists.
#        lines = line1 + line2
#        # Use list comprehension to get the label names we set in the plot
#        # call and add them to a list to pass along to the legend call.
#        labels = [l.get_label() for l in lines]
        # Now we make the legend with the list of lines plotted (gets color)
        # and the label names we want to display.
#        axes.legend(lines, labels)

    # ---- (6) ---- #
    # Why does the second yaxis not get a label?
    # Also can I make that label match the line color?
    if False:
        y_label2 = met_ds[var_name2].attrs['long_name']
        y_label2 = y_label2 + ' (' + met_ds[var_name2].attrs['units'] + ')'
        axes_right.set_ylabel(y_label2, color=line2_color)

    # ---- (7) ---- #
    # The xaxis shares the same values but we updated the orginal format
    # of the axis. The right plot did not update the plot for the xaxis for us.
    # To get the axis to look correct just update the xaxis again.
    if False:
        axes.xaxis.set_major_formatter(myFmt)

    # ---- (8) ---- #
    # And the most important part of all, a title.
    if False:
        axes.set_title(('An amazing plot of Temp. and RH. '
                        'on {}').format(first_time.astype('datetime64[D]')))

    # ---- (9) ---- #
    if False:
        # Save the figure to a file
        plt.savefig('temperature_plot.jpg')
    else:
        plt.show()  # Show the plot in a new window
