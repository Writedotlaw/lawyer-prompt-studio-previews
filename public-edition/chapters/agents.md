# Supervise the assignment as well as the answer.
> An AI agent can work through several actions before returning a result. Decide what it may do, what evidence it must preserve, and where the work must come back to a person.
@nav Supervise AI agents

## Give the system only the authority the assignment needs.

An agent might search approved documents, compare what it finds, and prepare a draft without asking you to start each step. That can be useful when the sequence is clear. It also means that important choices may occur before you see the final page.

In the vendor matter, reading correspondence is different from contacting the vendor. Preparing a recommendation is different from emailing it to the client. Decide which actions belong in the assignment and which require separate approval. Access should follow that decision rather than expand to include every feature the product offers.

Also decide what you need to inspect along the way. A polished recommendation may conceal an unsupported date used several steps earlier. Requiring a source-linked timeline before the comparison gives you a place to find that problem while it is still easy to correct.

## Write the assignment before launching the agent.

A work order is a written assignment with the details a multi-step task needs. It describes the intended result and scope, identifies sources and permitted tools, and explains what the system should return. It also records the evidence requirements, prohibited actions, stopping conditions, approvals, tests, and recordkeeping appropriate to the work.

The form below keeps those twelve subjects together. Start with the supplied vendor example to see how they fit, or describe a fictional assignment of your own. Give concrete answers where an instruction matters. “Use only these documents” is more useful when the documents are identified. “Stop if uncertain” is more useful when it names the missing information or conflict that requires review.

Completing the form produces instructions you can copy or download. It does not start an agent or configure permissions in another product. Review the assignment, then implement and test the relevant controls in the authorized system you use.

{{widget:workorder}}

## Look for the error that made the final answer possible.

When a result goes wrong, work backward. Did the system misunderstand the goal? Did a source go missing? Did an allegation become an accepted fact? An early mistake can supply the premise for several later steps, so editing the last paragraph may leave the cause untouched.

Consider an agent asked to recommend the fastest way to resolve a dispute. It may produce an answer that favors speed while overlooking the client's need to preserve a commercial relationship. The problem began in the objective. Another agent may accurately compare the sources it retrieved but omit the amendment that changes the result. That problem began in the source collection or retrieval step.

Use the workflow to decide where the issue should have surfaced. A required source list can reveal a missing amendment. A lawyer's review of the proposed objective can expose the tradeoff hidden in “fastest.” The useful control addresses the particular failure rather than adding a general demand for accuracy to every prompt.

## Test whether the software enforces the important limits.

A written prohibition tells the system what you expect. A technical restriction limits what it can do. For consequential actions, find out which protection the application provides and how it behaves when approval is missing.

Test the boundary with a safe example. Ask the system to prepare an internal comparison, then introduce a request to send it externally. Does sending remain blocked? If a retrieved document contains instructions to ignore the assignment or reveal unrelated information, are those instructions treated as untrusted source content? This problem is called **prompt injection**. It is a reason to limit permissions and test the system, not merely add a warning to the prompt.

Keep the route back to a person explicit. Name who reviews the question, what information they receive, and what authorization is needed to continue. An agent's statement that it is confident cannot substitute for a decision the assignment reserves to a lawyer.

## Include examples where stopping is the correct result.

A useful test has an expected outcome. With a missing amendment, the system should identify the gap and avoid claiming a complete review of the contract. With conflicting dates, it should preserve the conflict and ask for the specified decision. With an unapproved external action, it should stop before taking it.

Test ordinary assignments as well. A system that refuses everything would avoid some errors while failing to do the work. You need evidence that it completes the intended tasks and handles their limits appropriately. Keep representative examples and known failures so you can rerun them after changing instructions, sources, or the underlying product.

Record what happened, including failures and the review they required. That record helps you decide whether to revise the workflow, narrow its use, or stop using it for the task. The [testing worksheet](#/lab/shipping) gives you a place to organize the evidence and remaining questions.
