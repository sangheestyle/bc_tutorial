#!/usr/bin/perl
use strict;
use warnings;

use DB_File;
use Parallel::ForkManager;

# takes long long time subroutine!
sub square {
  sleep(5);
  $_[0] * $_[0];
}


# Limit for cores for multiprocessing
my $MAX_PROCESSES = 7;
my $pm = new Parallel::ForkManager($MAX_PROCESSES);

my @data = (1..8);

# For sharing values between processes
tie my %output, "DB_File", "output.dat";

foreach my $val (@data) {
  # Parallel processing
  my $pid = $pm->start and next;
    print ">>> $val\n";
    $output{$val} = square($val);
    print "<<< $val, $output{$val}\n";
  $pm->finish;
}
# Wait for all the children process to be done
$pm->wait_all_children;

# Sum
my $total = 0;
foreach my $val (values %output) {
  $total += $val;
}

print "sum: $total\n";
print "Done!\n";
