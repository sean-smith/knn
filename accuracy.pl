#!/usr/bin/perl

my $sum = 0;
my $count = 0;
while (<>) {
	my ($var1, $var2) = ($_ =~ m/(.),(.)$/);
	if ($var1 eq $var2) {
		#print "$var1 = $var2\n";
		$sum++;	
	}
	$count++;
}
print "Accuracy is:\n";
print $sum/$count . "\n";
