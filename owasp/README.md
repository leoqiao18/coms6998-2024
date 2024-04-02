# OWASP

This directory contains results from running CodeQL on the [OWASP BenchmarkJava repo](https://github.com/OWASP-Benchmark/BenchmarkJava) version 1.2.

The `expectedresults-1.2.csv` is copied from the BenchmarkJava repo. It contains the true values for true-positives and false-positives.

__TLDR:__ `codeql-cwe-78.csv` contains the results of comparing CodeQL analysis output with the expected results for CWE-78.

## CodeQL results

The results in this directory is generated with the following process. If you want to replicate the process, follow the following steps.

### 1. `Benchmark_1.2-codeql_java-security-and-quality.sarif`

SARIF (Static Analysis Results Interchange Format) standard is used to streamline how static analysis tools share their results. CodeQL outputs analysis results in this format.

To generate the analysis result, do the following steps:

1. Clone the [OWASP BenchmarkJava repo](https://github.com/OWASP-Benchmark/BenchmarkJava)
2. Download the CodeQL CLI zip package, and extract the zip archieve. Place the extracted codeql directory in a tools/ directory that is a peer to the folder containing BenchmarkJava. For example, if you have a `git/` folder, which contains BenchmarkJava, BenchmarkUtils, etc., then the tools/ folder would be at the same level as the `git/` folder.  i.e., relative to BenchmarkJava, it is at `../../tools/code-ql-home`.
3. At the root of the BenchmarkJava repo, the owasp-benchmark database has to be initialized by running this:

```bash
../../tools/codeql-home/codeql/codeql database create owasp-benchmark --language=java
```

4. Perform the CodeQL analysis by doing either one of the following:

```bash
scripts/runCodeQLFull.sh
```

The result of the analysis is stored as `Benchmark_1.2-codeql_java-security-and-quality.sarif`.


### 2. (Optional) `codeql-analysis.csv`

In case you want to view the analysis results in CSV, we can convert `code-analysis.sarif` to `code-analysis.csv` with the following steps:

1. Install `sarif-tools` with `pip` or `pipx`. For example,

```bash
pip install sarif-tools
```

2. Convert the CodeQL analysis results from `.sarif` to `.csv`:

```bash
sarif csv code-analysis.sarif --output codeql-analysis.csv
```

This outputs the desired `codeql-analysis.csv` file in the current directory.


### 3. `Benchmark_v1.2_Scorecard_for_CodeQL_v2.16.6.csv`

This file contains the metrics of comparing CodeQL analysis results with the expected results. To generate this file, do the following:

1. At the root of the BenchmarkJava repo, do:

```bash
./createScorecards.sh
```

__NOTE:__ You might run into some errors saying `Required plugin: org.owasp:benchmarkutils-maven-plugin not available.`. This can be resolved by following the helpful message in the error and performing the following:

```bash
git clone https://github.com/OWASP-Benchmark/BenchmarkUtils.git
cd BenchmarkUtils
mvn install
```

2. A graphycal display of the analysis results is at `scorecard/Benchmark_v1.2_Scorecard_for_CodeQL_v2.16.6.html` and can be viewed with a browser. The raw results are in `scorecard/Benchmark_v1.2_Scorecard_for_CodeQL_v2.16.6.csv`.


### 4. `codeql-cwe-78.csv`

From the `Benchmark_v1.2_Scorecard_for_CodeQL_v2.16.6.csv`, since we are particularly interested in CWE-78, I extracted the results for CWE-78 and put it in `codeql-cwe-78.csv`.