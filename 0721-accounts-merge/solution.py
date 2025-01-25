# Approach 1: Depth First Search

# n = no. of accounts, k = max length of account
# Time: O(n * k * log (nk))
# Space: O(nk)

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # create email to name mapping
        email_to_name = {}
        # create email graph
        email_graph = {}

        # Build the graph
        for account in accounts:
            name = account[0]
            # process all emails in the account
            for email in account[1:]:
                email_to_name[email] = name
                if email not in email_graph:
                    email_graph[email] = set()

                # connect first email with all other emails in the account
                if len(account) > 2:
                    email_graph[account[1]].add(email)
                    email_graph[email].add(account[1])

        # DFS function to find all connected emails
        def dfs(email, visited, connected_emails):
            visited.add(email)
            connected_emails.append(email)
            for neighbor in email_graph[email]:
                if neighbor not in visited:
                    dfs(neighbor, visited, connected_emails)

        # Process all emails and merge accounts
        visited = set()
        merged_accounts = []

        for email in email_graph:
            if email not in visited:
                connected_emails = []
                dfs(email, visited, connected_emails)
                merged_accounts.append([email_to_name[email]] + sorted(connected_emails))

        return merged_accounts
