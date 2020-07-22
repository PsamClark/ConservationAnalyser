# ConservationAnalyser
Function for determining conservation of a subsequence across multiple aligned DNA or RNA sequences.

## Installation

The MotiF library can be found within the `ConservationAnalyser.py` file in the `lib` directory and requires the following software versions:


- `Python`: *2.7*
- `NumPy`: *1.16.3* 
- `Bio`: *1.73*

To install add the location of this file to your `PYTHONPATH` and you are good to: ` from ConservationAnalyser import ConservationAnalyser`

## Usage

Once the package has been imported the function can be called using the following command: `ConservationAnalyser(seq_file,subseq,start_pos)`

where `seq_file` is a fasta file with aligned sequences,`subseq` is the subsequence over which conservation is assessed and `start_pos` is the position of the subsequence in the reference genome.

The returned value is average conservation across the subsequence

Please note that the reference sequence should be the first sequence in `seq_file`.

## Contributions
 
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.
  
## License

[MIT](LICENSE)
