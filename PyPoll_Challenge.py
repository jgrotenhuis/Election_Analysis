# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a total vote counter.
total_votes = 0
# Candidate options, county options, candidate votes, and county votes.
county_options = []
candidate_options = []
candidate_votes = {}
county_votes = {}
# Track the winning candidate, vote count, and percentage.
largest_county_turnout = ""
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read and print the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes  += 1
        # Print the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate add it the
        # the candidate list.
        # Print the county name from each row
        county_name = row[1]

        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        # Add a vote to the candidate's count.
        candidate_votes[candidate_name] += 1
        
        if county_name not in county_options:
            # Add it to the dictionary of counties
            county_options.append(county_name)
            # Begin tracking that county's vote count.
            county_votes[county_name] = 0
        county_votes[county_name] += 1
        
# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f"\nCounty Votes:\n")
    print(election_results, end="")
    txt_file.write(election_results)
    for county in county_votes:
        # Retrieve the vote count and percentage.
        votes = county_votes[county]
        vote_percentage = (int(votes) / int(total_votes)) * 100
        county_results = (
            f"{county}: {vote_percentage:.1f}% ({votes:,})\n")
        
        # Print each county's voter count and percentage to the terminal.
        print(county_results)
        # Save the county results to our text file.
        txt_file.write(county_results)
        # Determine the winning county by vote count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            largest_county_turnout = county

    winning_county_summary = (
        f"-------------------------\n"
        f"Largest County Turnout: {largest_county_turnout}\n"
        f"-------------------------\n")
    print(winning_county_summary)
    # Save the winning county's results to the text file.
    txt_file.write(winning_county_summary)
    
    winning_count = 0

    for candidate in candidate_votes:
        # Retrieve the vote count and percentage.
        votes = candidate_votes[candidate]
        vote_percentage = (int(votes) / int(total_votes)) * 100
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)