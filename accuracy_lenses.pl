#!/usr/bin/perl

my $sum = 0;
my $count = 0;
while (<>) {
	my ($var1, $var2) = ($_ =~ m/,(\d),([\d]).0/);
	print "$var1\n";
	print "$var2\n";
	if ($var1 eq $var2) {
		$sum++;	
	}
	$count++;
}
print "Accuracy is:\n";
print $sum/$count . "\n";
