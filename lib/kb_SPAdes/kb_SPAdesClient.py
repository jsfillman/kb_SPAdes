# -*- coding: utf-8 -*-
############################################################
#
# Autogenerated by the KBase type compiler -
# any changes made here will be overwritten
#
############################################################

from __future__ import print_function
# the following is a hack to get the baseclient to import whether we're in a
# package or not. This makes pep8 unhappy hence the annotations.
try:
    # baseclient and this client are in a package
    from .baseclient import BaseClient as _BaseClient  # @UnusedImport
except ImportError:
    # no they aren't
    from baseclient import BaseClient as _BaseClient  # @Reimport


class kb_SPAdes(object):

    def __init__(
            self, url=None, timeout=30 * 60, user_id=None,
            password=None, token=None, ignore_authrc=False,
            trust_all_ssl_certificates=False,
            auth_svc='https://ci.kbase.us/services/auth/api/legacy/KBase/Sessions/Login'):
        if url is None:
            raise ValueError('A url is required')
        self._service_ver = None
        self._client = _BaseClient(
            url, timeout=timeout, user_id=user_id, password=password,
            token=token, ignore_authrc=ignore_authrc,
            trust_all_ssl_certificates=trust_all_ssl_certificates,
            auth_svc=auth_svc)

    def run_SPAdes(self, params, context=None):
        """
        Run SPAdes on paired end libraries
        :param params: instance of type "SPAdesParams" (Input parameters for
           running SPAdes. workspace_name - the name of the workspace from
           which to take input and store output. output_contigset_name - the
           name of the output contigset read_libraries - a list of Illumina
           PairedEndLibrary files in FASTQ or BAM format. dna_source -
           (optional) the source of the DNA used for sequencing
           'single_cell': DNA amplified from a single cell via MDA anything
           else: Standard DNA sample from multiple cells. Default value is
           None. min_contig_length - (optional) integer to filter out contigs
           with length < min_contig_length from the SPAdes output. Default
           value is 0 implying no filter. kmer_sizes - (optional) K-mer
           sizes, Default values: 33, 55, 77, 99, 127 (all values must be
           odd, less than 128 and listed in ascending order) In the absence
           of these values, K values are automatically selected.
           skip_error_correction - (optional) Assembly only (No error
           correction). By default this is disabled.) -> structure: parameter
           "workspace_name" of String, parameter "output_contigset_name" of
           String, parameter "read_libraries" of list of type
           "paired_end_lib" (The workspace object name of a PairedEndLibrary
           file, whether of the KBaseAssembly or KBaseFile type.), parameter
           "dna_source" of String, parameter "min_contig_length" of Long,
           parameter "kmer_sizes" of list of Long, parameter
           "skip_error_correction" of type "bool" (A boolean. 0 = false,
           anything else = true.)
        :returns: instance of type "SPAdesOutput" (Output parameters for
           SPAdes run. report_name - the name of the KBaseReport.Report
           workspace object. report_ref - the workspace reference of the
           report.) -> structure: parameter "report_name" of String,
           parameter "report_ref" of String
        """
        return self._client.call_method('kb_SPAdes.run_SPAdes',
                                        [params], self._service_ver, context)

    def run_HybridSPAdes(self, params, context=None):
        """
        Run HybridSPAdes on paired end libraries with PacBio CLR and Oxford Nanopore reads
        :param params: instance of type "HybridSPAdesParams" (------To run
           HybridSPAdes 3.13.0 you need at least one library of the following
           types:------ 1) Illumina paired-end/high-quality
           mate-pairs/unpaired reads 2) IonTorrent paired-end/high-quality
           mate-pairs/unpaired reads 3) PacBio CCS reads Version 3.13.0 of
           SPAdes supports paired-end reads, mate-pairs and unpaired reads.
           SPAdes can take as input several paired-end and mate-pair
           libraries simultaneously. workspace_name - the name of the
           workspace from which to take input and store output.
           output_contigset_name - the name of the output contigset
           read_libraries - a list of Illumina or IonTorrent
           paired-end/high-quality mate-pairs/unpaired reads
           long_reads_libraries - a list of PacBio, Oxford Nanopore Sanger
           reads and/or additional contigs dna_source - the source of the DNA
           used for sequencing 'single_cell': DNA amplified from a single
           cell via MDA anything else: Standard DNA sample from multiple
           cells. Default value is None. pipeline_options - a list of string
           specifying how the SPAdes pipeline should be run kmer_sizes -
           (optional) K-mer sizes, Default values: 21, 33, 55, 77, 99, 127
           (all values must be odd, less than 128 and listed in ascending
           order) In the absence of these values, K values are automatically
           selected. min_contig_length - integer to filter out contigs with
           length < min_contig_length from the HybridSPAdes output. Default
           value is 0 implying no filter. @optional dna_source @optional
           pipeline_options @optional kmer_sizes @optional min_contig_length)
           -> structure: parameter "workspace_name" of String, parameter
           "output_contigset_name" of String, parameter "reads_libraries" of
           list of type "ReadsParams" (parameter groups--define attributes
           for specifying inputs with YAML data set file (advanced) The
           following attributes are available: - orientation ("fr", "rf",
           "ff") - type ("paired-end", "mate-pairs", "hq-mate-pairs",
           "single", "pacbio", "nanopore", "sanger", "trusted-contigs",
           "untrusted-contigs") - interlaced reads (comma-separated list of
           files with interlaced reads) - left reads (comma-separated list of
           files with left reads) - right reads (comma-separated list of
           files with right reads) - single reads (comma-separated list of
           files with single reads or unpaired reads from paired library) -
           merged reads (comma-separated list of files with merged reads)) ->
           structure: parameter "lib_ref" of type "obj_ref" (An X/Y/Z style
           KBase object reference), parameter "orientation" of String,
           parameter "lib_type" of String, parameter "long_reads_libraries"
           of list of type "LongReadsParams" -> structure: parameter
           "long_reads_ref" of type "obj_ref" (An X/Y/Z style KBase object
           reference), parameter "long_reads_type" of String, parameter
           "dna_source" of String, parameter "pipeline_options" of list of
           String, parameter "kmer_sizes" of list of Long, parameter
           "min_contig_length" of Long, parameter "create_report" of type
           "bool" (A boolean. 0 = false, anything else = true.)
        :returns: instance of type "SPAdesOutput" (Output parameters for
           SPAdes run. report_name - the name of the KBaseReport.Report
           workspace object. report_ref - the workspace reference of the
           report.) -> structure: parameter "report_name" of String,
           parameter "report_ref" of String
        """
        return self._client.call_method('kb_SPAdes.run_HybridSPAdes',
                                        [params], self._service_ver, context)

    def run_metaSPAdes(self, params, context=None):
        """
        Run SPAdes on paired end libraries for metagenomes
        :param params: instance of type "SPAdesParams" (Input parameters for
           running SPAdes. workspace_name - the name of the workspace from
           which to take input and store output. output_contigset_name - the
           name of the output contigset read_libraries - a list of Illumina
           PairedEndLibrary files in FASTQ or BAM format. dna_source -
           (optional) the source of the DNA used for sequencing
           'single_cell': DNA amplified from a single cell via MDA anything
           else: Standard DNA sample from multiple cells. Default value is
           None. min_contig_length - (optional) integer to filter out contigs
           with length < min_contig_length from the SPAdes output. Default
           value is 0 implying no filter. kmer_sizes - (optional) K-mer
           sizes, Default values: 33, 55, 77, 99, 127 (all values must be
           odd, less than 128 and listed in ascending order) In the absence
           of these values, K values are automatically selected.
           skip_error_correction - (optional) Assembly only (No error
           correction). By default this is disabled.) -> structure: parameter
           "workspace_name" of String, parameter "output_contigset_name" of
           String, parameter "read_libraries" of list of type
           "paired_end_lib" (The workspace object name of a PairedEndLibrary
           file, whether of the KBaseAssembly or KBaseFile type.), parameter
           "dna_source" of String, parameter "min_contig_length" of Long,
           parameter "kmer_sizes" of list of Long, parameter
           "skip_error_correction" of type "bool" (A boolean. 0 = false,
           anything else = true.)
        :returns: instance of type "SPAdesOutput" (Output parameters for
           SPAdes run. report_name - the name of the KBaseReport.Report
           workspace object. report_ref - the workspace reference of the
           report.) -> structure: parameter "report_name" of String,
           parameter "report_ref" of String
        """
        return self._client.call_method('kb_SPAdes.run_metaSPAdes',
                                        [params], self._service_ver, context)

    def estimate_metaSPAdes_requirements(self, params, context=None):
        """
        :param params: instance of type "MetaSPAdesEstimatorParams" (params -
           the params used to run metaSPAdes. use_defaults - (optional, def
           0) if 1, just return the default requirements use_heuristic -
           (optional, def 1) if 1, only use a heuristic based on the reads
           metadata to perform estimates) -> structure: parameter "params" of
           type "SPAdesParams" (Input parameters for running SPAdes.
           workspace_name - the name of the workspace from which to take
           input and store output. output_contigset_name - the name of the
           output contigset read_libraries - a list of Illumina
           PairedEndLibrary files in FASTQ or BAM format. dna_source -
           (optional) the source of the DNA used for sequencing
           'single_cell': DNA amplified from a single cell via MDA anything
           else: Standard DNA sample from multiple cells. Default value is
           None. min_contig_length - (optional) integer to filter out contigs
           with length < min_contig_length from the SPAdes output. Default
           value is 0 implying no filter. kmer_sizes - (optional) K-mer
           sizes, Default values: 33, 55, 77, 99, 127 (all values must be
           odd, less than 128 and listed in ascending order) In the absence
           of these values, K values are automatically selected.
           skip_error_correction - (optional) Assembly only (No error
           correction). By default this is disabled.) -> structure: parameter
           "workspace_name" of String, parameter "output_contigset_name" of
           String, parameter "read_libraries" of list of type
           "paired_end_lib" (The workspace object name of a PairedEndLibrary
           file, whether of the KBaseAssembly or KBaseFile type.), parameter
           "dna_source" of String, parameter "min_contig_length" of Long,
           parameter "kmer_sizes" of list of Long, parameter
           "skip_error_correction" of type "bool" (A boolean. 0 = false,
           anything else = true.), parameter "use_defaults" of Long
        :returns: instance of type "MetaSPAdesEstimate" (cpus - the number of
           CPUs required for the run memory - the minimal amount of memory in
           MB required for the run walltime - an estimate for walltime in
           seconds for the run) -> structure: parameter "cpus" of Long,
           parameter "memory" of Long, parameter "walltime" of Long
        """
        return self._client.call_method('kb_SPAdes.estimate_metaSPAdes_requirements',
                                        [params], self._service_ver, context)

    def status(self, context=None):
        return self._client.call_method('kb_SPAdes.status',
                                        [], self._service_ver, context)
