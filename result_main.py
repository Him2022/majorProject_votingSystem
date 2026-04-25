import time
import matplotlib.pyplot as plt

# ✅ IMPORT FROM CORRECT FILE
from ring_signature import generate_voter_keypair, ring_sign, ring_verify, hash_mod_p


# ---------------- BENCHMARK WITH AVERAGING ----------------
def benchmark(voter_counts, runs=5):
    results = []

    for count in voter_counts:
        print(f"Benchmarking {count} voters...")

        kg_list, sg_list, sv_list = [], [], []

        for _ in range(runs):

            # 1. Key Generation
            start = time.perf_counter()
            keys = [generate_voter_keypair() for _ in range(count)]
            pks = [k[1] for k in keys]
            kg_list.append((time.perf_counter() - start) * 1000)

            # 2. Signature Generation
            msg_hash = hash_mod_p("sample_vote")
            start = time.perf_counter()
            sig = ring_sign(msg_hash, pks, 0, keys[0][0])
            sg_list.append((time.perf_counter() - start) * 1000)

            # 3. Verification
            start = time.perf_counter()
            ring_verify(msg_hash, sig, pks)
            sv_list.append((time.perf_counter() - start) * 1000)

        # ✅ AVERAGE TIMES
        avg_kg = sum(kg_list) / runs
        avg_sg = sum(sg_list) / runs
        avg_sv = sum(sv_list) / runs

        results.append({
            "voters": count,
            "keygen": avg_kg,
            "sign": avg_sg,
            "verify": avg_sv,
            "total": avg_kg + avg_sg + avg_sv
        })

    return results


# ---------------- RUN ----------------
voter_counts = [10, 50, 100, 200]
results = benchmark(voter_counts, runs=5)


# ---------------- PRINT RESULTS ----------------
print("\nBenchmark Results:")
for r in results:
    print(r)


# ---------------- EXTRACT ----------------
voters = [r["voters"] for r in results]
keygen_time = [r["keygen"] for r in results]
sign_time = [r["sign"] for r in results]
verify_time = [r["verify"] for r in results]
total_time = [r["total"] for r in results]


# ---------------- GRAPH 1 ----------------
plt.figure(figsize=(10, 6))

plt.plot(voters, keygen_time, label='Key Generation', marker='o')
plt.plot(voters, sign_time, label='Ring Signing', marker='s')
plt.plot(voters, verify_time, label='Ring Verification', marker='^')

plt.title('Average Performance Analysis vs Number of Voters')
plt.xlabel('Number of Voters')
plt.ylabel('Time (ms)')
plt.grid(True)
plt.legend()

plt.savefig('performance_analysis.png', dpi=300)
plt.show()


# ---------------- GRAPH 2 ----------------
plt.figure(figsize=(10, 6))

plt.plot(voters, total_time, label='Total Execution Time', marker='D')

plt.title('Average Total Execution Time vs Voters')
plt.xlabel('Number of Voters')
plt.ylabel('Time (ms)')
plt.grid(True)
plt.legend()

plt.savefig('total_execution_time.png', dpi=300)
plt.show()


# ---------------- GRAPH 3 (NEW: TIME PER VOTER) ----------------
plt.figure(figsize=(10, 6))

time_per_voter = [t / v for t, v in zip(total_time, voters)]

plt.plot(voters, time_per_voter, marker='o', linewidth=2)

plt.title('Average Time per Voter vs Number of Voters')
plt.xlabel('Number of Voters')
plt.ylabel('Time per Voter (ms)')
plt.grid(True)

plt.savefig('time_per_voter.png', dpi=300)
plt.show()


print("All graphs generated successfully ✅")