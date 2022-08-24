#! /usr/bin/perl
use POSIX;
use strict;

print "Perl version $]\n";
$| = 1;

if ( @ARGV != 1 ) {print "\nMust pass in one argument only - an input file\n"; exit(1); }

my $inFile = shift(@ARGV);
my $outFile= $inFile."_output";

{
    if(!&doSomething(@ARGV)){ exit(1); }
    exit(0);
}

sub doSomething {

    my $record=""; my $recI=0; my $recO=0; my $recB=0; my $mod=0;

    my $ClientTrackingNumber; my $ClientSourceCode; my $FullName; my $CompanyName; my $Address1; my $Address2; my $City; my $State; my $PostalCode;

    unless (open(IFILE,"$inFile"  )){ print("ERROR: Can't open: $inFile\n" ); return 0; }
    unless (open(OFILE,">$outFile")){ print("ERROR: Can't open: $outFile\n"); return 0; }

    while ( $record = <IFILE> ) {

	$recI++;

	( $ClientTrackingNumber,$ClientSourceCode,$FullName,$CompanyName,$Address1,$Address2,$City,$State,$PostalCode ) = split (/\|/, $record);

        if (( $FullName =~ ( /([a-hA-H])\1\1\1/ )) || 
	    ( $FullName =~ ( /([j-zJ-Z])\1\1\1/ ))) {

	    print ">BAD > $ClientTrackingNumber > $FullName\n";
	    $recB++;
	} else {
	    print OFILE "$record";
	    $recO++;
	}

	$mod = $recI%100000000;
	if (!$mod) { print ">$recI processed\n"; }
	# if ($recI>=100000) { return(0); }

    } # end while

    print "Records read  : $recI\n";
    print "Records write : $recO\n";

    close (IFILE);
    close (OFILE);

    return(0);

}

# eof
