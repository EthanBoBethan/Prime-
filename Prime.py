import time
import math
import sys

# ==========================================
# ULTIMATE PRIME SEARCHER
# ==========================================

print("=" * 40)
print("ULTIMATE PRIME SEARCHER")
print("=" * 40)
print("1) Run for a set time")
print("2) Search until a target number")
print("3) Search until stopped manually")
print()

mode = input("Choose mode (1/2/3): ").strip()

target_time = None
target_number = None

if mode == "1":
    target_time = float(input("Runtime (seconds): "))

elif mode == "2":
    target_number = int(input("Target number: "))

elif mode == "3":
    print("\nPress Ctrl+C to stop.\n")

else:
    print("Invalid mode.")
    sys.exit()

# ==========================================
# PRIME TEST
# ==========================================

def is_prime(n, primes):
    limit = math.isqrt(n)

    for p in primes:
        if p > limit:
            return True

        if n % p == 0:
            return False

    return True

# ==========================================
# SEARCH
# ==========================================

UPDATE_INTERVAL = 0.05

start_time = time.perf_counter()
next_update = start_time + UPDATE_INTERVAL

primes = [2]
candidate = 3

largest_gap = 0

try:
    while True:

        now = time.perf_counter()
        elapsed = now - start_time

        # ----------------------
        # STOP CONDITIONS
        # ----------------------

        if mode == "1":
            if elapsed >= target_time:
                break

        elif mode == "2":
            if candidate > target_number:
                break

        # ----------------------
        # PRIME TEST
        # ----------------------

        limit = math.isqrt(candidate)
        prime = True

        for p in primes:
            if p > limit:
                break

            if candidate % p == 0:
                prime = False
                break

        if prime:

            gap = candidate - primes[-1]

            if gap > largest_gap:
                largest_gap = gap

            primes.append(candidate)

        candidate += 2

        # ----------------------
        # STATUS BAR
        # ----------------------

        if now >= next_update:

            if mode == "1":

                progress = min(elapsed / target_time, 1.0)

                bar_len = 40
                filled = int(progress * bar_len)

                bar = (
                    "█" * filled
                    + "-" * (bar_len - filled)
                )

                print(
                    f"\r[{bar}] "
                    f"{progress*100:6.2f}% | "
                    f"{len(primes):,} primes | "
                    f"largest {primes[-1]:,}",
                    end="",
                    flush=True
                )

            elif mode == "2":

                progress = min(
                    candidate / target_number,
                    1.0
                )

                bar_len = 40
                filled = int(progress * bar_len)

                bar = (
                    "█" * filled
                    + "-" * (bar_len - filled)
                )

                print(
                    f"\r[{bar}] "
                    f"{progress*100:6.2f}% | "
                    f"{len(primes):,} primes | "
                    f"largest {primes[-1]:,}",
                    end="",
                    flush=True
                )

            else:

                print(
                    f"\r[RUNNING] "
                    f"{elapsed:8.2f}s | "
                    f"{len(primes):,} primes | "
                    f"largest {primes[-1]:,}",
                    end="",
                    flush=True
                )

            next_update += UPDATE_INTERVAL

except KeyboardInterrupt:
    print("\n\nStopping search...")

# ==========================================
# FINAL STATS
# ==========================================

runtime = time.perf_counter() - start_time

largest_prime = primes[-1]
prime_count = len(primes)

numbers_checked = candidate

# independent verification

def verify_prime(n):

    if n < 2:
        return False

    if n % 2 == 0:
        return n == 2

    limit = math.isqrt(n)

    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False

    return True

verified = verify_prime(largest_prime)

density = (
    prime_count / numbers_checked
) * 100

avg_primes_per_sec = (
    prime_count / runtime
)

avg_numbers_per_sec = (
    numbers_checked / runtime
)

memory_used_mb = (
    sum(sys.getsizeof(x) for x in primes)
    + sys.getsizeof(primes)
) / 1024 / 1024

print("\n")
print("=" * 50)
print(f"Runtime: {runtime:.3f} seconds")
print(f"Numbers checked: {numbers_checked:,}")
print(f"Primes found: {prime_count:,}")
print(f"Largest prime found: {largest_prime:,}")
print(f"Prime index: #{prime_count:,}")
print(
    f"Verification: "
    f"{'PASSED ✓' if verified else 'FAILED ✗'}"
)
print(f"Prime density: {density:.4f}%")
print(
    f"Average primes/sec: "
    f"{avg_primes_per_sec:,.0f}"
)
print(
    f"Numbers/sec: "
    f"{avg_numbers_per_sec:,.0f}"
)
print(
    f"Largest gap near end: "
    f"{largest_gap:,}"
)
print(
    f"Memory used by primes: "
    f"{memory_used_mb:.2f} MB"
)
print("=" * 50)
