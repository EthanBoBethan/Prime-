# Ultimate Prime Searcher

## Overview

Ultimate Prime Searcher is a high-performance Python program for discovering prime numbers. It can run for a specified amount of time, search up to a target number, or continue running until manually stopped.

The program tracks detailed statistics including:

* Total primes found
* Largest prime found
* Prime index
* Prime density
* Numbers checked
* Average primes per second
* Average numbers checked per second
* Largest prime gap found
* Memory usage
* Independent verification of the final prime

---

## Features

### Search Modes

#### 1. Timed Search

Run the search for a specific number of seconds.

Example:

```text
Runtime (seconds): 60
```

#### 2. Target Search

Search until a target number has been reached.

Example:

```text
Target number: 100000000
```

#### 3. Continuous Search

Run indefinitely until stopped by the user.

Example:

```text
Press Ctrl+C to stop.
```

---

## Requirements

* Python 3.9+
* No external libraries required

---

## Running the Program

Open a terminal and run:

```bash
python prime_searcher.py
```

Follow the on-screen prompts to select a search mode.

---

## Example Output

```text
==================================================
Runtime: 60.000 seconds
Numbers checked: 29,880,242
Primes found: 1,850,833
Largest prime found: 29,880,241
Prime index: #1,850,833
Verification: PASSED ✓
Prime density: 6.1942%
Average primes/sec: 30,847
Numbers/sec: 498,004
Largest gap near end: 72
Memory used by primes: 14.12 MB
==================================================
```

---

## Statistics Explained

### Numbers Checked

The largest range of numbers tested for primality.

### Primes Found

Total number of prime numbers discovered during the search.

### Largest Prime Found

The highest confirmed prime number discovered.

### Prime Index

The position of the largest prime within the ordered sequence of all discovered primes.

### Verification

Performs an independent primality check on the final prime found.

### Prime Density

The percentage of checked numbers that were prime.

Formula:

Prime Density = (Primes Found ÷ Numbers Checked) × 100

### Average Primes Per Second

The average rate at which primes were discovered.

### Numbers Per Second

The average rate at which candidate numbers were processed.

### Largest Prime Gap

The largest difference between two consecutive discovered primes.

### Memory Usage

Approximate memory consumed by stored prime numbers.

---

## Stopping a Search

For Continuous Search mode:

```text
Ctrl+C
```

The program will safely stop and display final statistics.

---

## Notes

* Larger runtimes generally produce larger primes.
* Prime density decreases as numbers become larger.
* Verification may take additional time for extremely large primes.
* Memory usage grows as more primes are stored.

---

## License

Free to use, modify, and distribute.

