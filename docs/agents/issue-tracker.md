# Issue tracker: GitHub

Issues, PRDs, Wayfinder maps, and decision tickets live as GitHub Issues in `jon-devlapaz/socraTink`. Use the `gh` CLI for all operations.

## Conventions

- Create: `gh issue create --title "..." --body "..."`
- Read: `gh issue view <number> --comments`
- List: `gh issue list --state open --json number,title,body,labels,assignees,url`
- Comment: `gh issue comment <number> --body "..."`
- Label: `gh issue edit <number> --add-label "..."`
- Claim: `gh issue edit <number> --add-assignee @me`
- Close: `gh issue close <number> --comment "..."`

Infer the repository from `git remote -v` when running inside the clone.

## Pull requests as a triage surface

**PRs as a request surface: no.**

## Skill publishing

When a skill says “publish to the issue tracker,” create a GitHub issue. When it says “fetch the relevant ticket,” use `gh issue view <number> --comments`.

## Wayfinding operations

- A map is one issue labelled `wayfinder:map`.
- Tickets are child issues labelled `wayfinder:research`, `wayfinder:prototype`, `wayfinder:grilling`, or `wayfinder:task`.
- Prefer GitHub sub-issues. If unavailable, put `Part of #<map>` in each ticket and list it as a task in the map.
- Prefer native issue dependencies. If unavailable, put `Blocked by: #<number>` in the ticket body.
- The frontier is the ordered set of open, unblocked, unassigned child tickets.
- Claim before work by assigning the ticket to yourself.
- Resolve by posting the answer as a comment, closing the ticket, and adding a linked gist to the map’s `Decisions so far` index.
