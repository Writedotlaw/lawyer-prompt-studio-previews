# Build a small version and test what it does.
> AI-assisted coding can help you explore a useful tool by describing its behavior. Your contribution begins with the problem, the requirements, and the tests that would reveal whether the idea works.
@nav Build and test a tool

## Treat the first version as a proposal to investigate.

Suppose your team repeatedly checks whether a document contains specified notice provisions. You might describe a tool that asks for those provisions and organizes them for a lawyer's review. A working prototype would let you examine whether that interface helps with the task.

It would not establish that the tool correctly understands every agreement, protects uploaded files, or is ready for clients to use. Those are separate questions that need evidence. A demonstration usually shows a selected example under selected conditions.

You may hear the term **vibe coding** for building through natural-language instructions and AI-generated code. For our purposes, the useful skill is translating a legal or practical need into behavior someone can observe and test. Start with fictional data and a limited purpose. Bring in appropriate technical expertise before another person depends on a system whose security or reliability you cannot assess.

## Describe the behavior instead of naming an impressive feature.

“Build a legal assistant” leaves most of the important decisions open. “Build a form that records the notice provision, flags a missing receipt date, and prepares a checklist for lawyer review” gives the builder something more definite to implement.

For each important feature, describe what the user supplies and what should happen. In the vendor example, what does the tool do when a date is missing? Does it distinguish sending from receipt? Can the user inspect the source supporting a result? Does the interface make an unresolved question look like a completed review?

Also describe what the tool must not do. A prototype for organizing notice information should not silently become a deadline calculator or an individualized recommendation to terminate. Legal rules often include conditions and exceptions that a neat interface can hide. Keep the proposed scope narrow enough that you can explain and test those boundaries.

## Prepare for review before anyone relies on the tool.

Use the worksheet below to record evidence and open questions about a proposed pilot. It asks about the intended users, legal logic, failure behavior, information handling, human review, and maintenance.

A checked box is your record that an area has been addressed, not an independent certification. Identify the test, source, or responsible reviewer behind it. Where something remains unresolved, describe the work needed before proceeding. Use only fictional or non-sensitive examples in this guide.

{{widget:shipping}}

## Write down what a test should show.

A test is more useful when you decide the expected behavior before running it. For a missing receipt date, you may expect a visible warning and no calculated cure-period conclusion. For conflicting documents, you may expect the tool to show the conflict and route it to a lawyer. For an ordinary complete example, you should expect it to perform the intended task without unnecessary refusal.

Include cases near the boundaries of the tool's scope and examples of failures you have already seen. Repeat important tests after a change. A clearer instruction or a new model can improve one result while creating another problem.

Test the experience as well as the answer. Ask someone who did not build the tool to use it without explanation. Can they find the source, understand the limitation, and tell what they should do next? A technically correct response can still mislead if the interface presents it as more conclusive than it is.

## Decide who will keep the tool fit for use.

Before a pilot begins, identify who can approve a change, investigate a failure, and withdraw a version that no longer works as intended. Someone also needs to watch for changes in the relevant law, sources, and software.

Make the user's route to a person understandable. A warning that says “consult a lawyer” may be inadequate if the service gives the user no practical way to do so. Where the workflow reserves a consequential decision for human review, that review needs to happen before the action, not after it.

Keep the first release limited to the purpose and evidence you can support. You can expand later when testing gives you a basis for it. A useful prototype is a way to learn about the problem and the proposed solution; preparing it for dependable use is further work that needs an owner.
