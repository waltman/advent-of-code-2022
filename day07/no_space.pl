#!/usr/bin/env perl
use v5.36;

package Dir;
use List::Util qw(sum);

sub new($package, $name, $parent) {
    my $self = {};
    bless $self, $package;

    $self->{name} = $name;
    $self->{parent} = $parent;
    $self->{files_size} = 0;
    $self->{children} = ();

    return $self;
}

sub size($self) {
    return $self->{files_size} + sum (map {$_->{files_size}} values %{$self->{children}});
}

my $root = Dir->new('/', undef);
my $pwd = $root;

while (<>) {
    chomp;
    my @toks = split ' ';
    if ($toks[0] eq '$') {
        if ($toks[1] eq 'cd') {
            if ($toks[2] eq '/') {
                $pwd = $root;
            } elsif ($toks[2] eq "..") {
                $pwd = $pwd->{parent};
            } else {
                $pwd = $pwd->{children}{$toks[2]};
            }
        } elsif ($toks[1] eq "dir") {
        }
    } else {
        if ($toks[0] eq "dir") {
            $pwd->{children}{$toks[1]} = Dir->new($toks[1], $pwd);
        } else {
            $pwd->{files_size} += $toks[0];
        }
    }
}

my $part1_sum;
my @queue = ($root);

while (@queue) {
    my $subdir = pop @queue;
    say "$subdir->{name}";
    my $size = $subdir->size();
    if ($size <= 100000) {
        $part1_sum += $size;
    }
    for my $child (values %{$subdir->{children}}) {
        push @queue, $child;
    }
}
