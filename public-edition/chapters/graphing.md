# Map the work before you ask AI to carry it out.
> Graphing an AI workflow means showing the tasks, what passes between them, and the decisions that determine what happens next. You can begin with a work plan on paper and run each step yourself.
@nav Map an AI workflow

## A workflow map makes the assignment easier to supervise.

Imagine asking AI to review a contract, read the correspondence, and recommend whether the client should terminate. That request leaves many decisions inside a single exchange. Which provisions matter? What does the correspondence establish? What should happen when a necessary fact is missing?

A workflow map brings those decisions into view. Each box names a task. A connecting line shows that one task needs something from another. A branch shows that the next step depends on what you find. For example, missing evidence might send the work back for investigation instead of forward to drafting.

The unfamiliar term is **graph**; the underlying skill is planning an assignment. Prompts give instructions for particular tasks. The map explains how those tasks fit together. A person can perform a task, an AI system can assist with it, or ordinary software can handle it. You do not need several AI agents to benefit from the plan.

## Begin with a defined question and appropriate materials.

We will use a fictional software-vendor matter. The client has reported service failures and wants advice about its options. The working materials include an agreement, an amendment, correspondence, and service records. For this example, assume the lawyer has also supplied the relevant governing-law analysis. Reviewing the contract alone would not resolve every legal question in an actual termination dispute.

The initial work plan separates two tasks. One identifies the contractual requirements. The other builds a factual timeline. Their findings then come together for a comparison that the lawyer reviews before choosing the approach to the recommendation.

Here is the important gap: the fictional contract measures the cure period from **receipt** of written notice, but the initial packet establishes only that an email was **sent**. The workflow needs somewhere for that difference to become visible and someone responsible for deciding what to do about it.

## Work through the example and examine the handoffs.

The exercise below shows how the assignment can proceed. Select a task to inspect its instructions, or choose “Begin the example” to move through the prepared sequence. Inspecting a task does not complete it.

When you reach the missing-receipt issue, decide whether to investigate further or approve a qualified approach. Later, introduce the new evidence and notice which work needs reconsideration. Adding a document does not approve the conclusion someone draws from it.

Everything in this demonstration is prewritten. It illustrates the decisions in a workflow; it does not review documents, run AI, or decide an actual matter.

{{widget:graph}}

## Give each task a result the next person can use.

A box labeled “Analyze the contract” is a start, but it leaves the assignment vague. Explain the question, identify the permitted materials, and describe what should come out of the task. Include what to do when the task cannot be completed as requested.

For the initial contract review, the assignment could require a table identifying each relevant termination condition, the language supporting it, and its source location. The table should preserve exceptions and point out any missing referenced material. It should not yet conclude that the client has met the conditions.

Now the next reviewer knows what they are receiving. They can compare a requirement with the factual record, inspect the supporting provision, and see which questions remain unresolved. This is what a useful handoff accomplishes: it preserves enough of the work for someone else to examine and continue it.

The task's review requirement should be equally concrete. Before the findings are used in a recommendation, the lawyer checks the relevant provisions and resolves material questions about how the agreement and amendment fit together.

## Keep the initial source review separate from the recommendation.

The contract review asks what the documents require. The timeline asks what the records show happened. Keeping those initial jobs distinct helps you inspect the basis for the later comparison.

```prompt
Read the agreement and amendment together. Identify the provisions relevant to termination for the reported service failures. For each requirement, give the relevant language and location, including exceptions or qualifications. Identify uncertainty about how the provisions fit together and anything you could not review. Do not decide whether the client has satisfied the requirements yet.
```

```prompt
Build a timeline from the supplied records and correspondence. Cite the document and location supporting each entry. Distinguish what a source establishes from what someone alleges, and preserve conflicting accounts. Identify missing information. Do not treat evidence that notice was sent as evidence of receipt or conclude that a contractual requirement has been satisfied.
```

You can run these requests in ordinary chats, one after the other. Give each the shared assignment and the materials it needs. Save the useful outputs with their source references. When you ask for the comparison, provide both sets of findings and access to the originals. The map does not require automation; at this stage, you are managing the handoffs yourself.

## Pass the uncertainty forward with the finding.

“Notice sent June 4” and “notice received June 4” are different findings. A handoff containing only “Notice: June 4” conceals that difference. The next task may calculate from the date without realizing what the evidence actually supports.

Require the comparison to connect each proposed conclusion with a contractual requirement and supporting evidence. When the support is incomplete, say what remains missing. A later drafting request should receive that qualification along with the lawyer's decision about how to handle it.

```prompt
Compare the contractual requirements with the factual findings. For each proposed conclusion, identify the supporting provision and record source. Preserve disputed facts and missing evidence. Do not resolve a material gap by assumption. Return the comparison and the questions the lawyer needs to decide before drafting advice.
```

Suppose the lawyer approves seeking an acknowledgment of receipt before recommending termination. That decision belongs in the next task's instructions. Otherwise, the drafting step may quietly replace it with a more confident conclusion. A short record of approved decisions can prevent the same issue from being reopened without anyone noticing.

## Separate tasks where separation improves the work.

Ask what a task must receive before it can begin. The initial factual timeline does not require the completed contract analysis. The recommendation needs both, together with the lawyer's decisions. That dependency gives you a reason to delay drafting until the comparison has been reviewed.

Separate work need not happen simultaneously. You can test the plan manually before considering software that runs suitable tasks at the same time. The first question is whether each task has a clear job and returns something useful.

Be careful with issues that are closely connected. Reviewing several agreements separately may help you organize their provisions, but someone still needs to examine how they interact. A task map should make that combined review explicit. Dividing the work is useful only when the plan also brings the necessary relationships back together.

## Define the final review before you rely on the draft.

“Check your work” does not tell a reviewer what to compare or what would count as a material problem. For this recommendation, the reviewer needs the underlying sources, approved findings, and the lawyer's instructions.

```prompt
Compare the draft with the underlying documents, approved findings, and my decisions. Identify unsupported assertions, omitted qualifications, and passages that treat an unresolved question as settled. For each issue, quote the draft language, identify the relevant source and location, and propose a correction or a question for me. Report anything you could not check.
```

Review the important findings yourself. An additional AI review can help identify a problem, but another generated assertion is not proof that the source supports the claim. Use an appropriate check for the question: arithmetic may need a calculator; a statement about receipt needs evidence; a recommendation needs judgment about what the client should do.

Also decide when the revision cycle ends. You might allow a correction round after source review, then require the lawyer to resolve any remaining material issues. Repeatedly asking the system to review itself until it declares success gives you no independent stopping standard.

## Test the map before automating it.

Compare your mapped approach with a simpler request using the same materials. Did the map expose a meaningful gap? Did it reduce overstatement? How much time did the lawyer spend checking and repairing the result? One successful example is a reason to keep testing, not a guarantee that the process will work on every matter.

Then change the facts. When the new email establishes receipt, the timeline and comparison need updating, followed by reconsideration of the recommendation and final review. The contract extraction may remain useful, subject to checking whether the new evidence makes another provision relevant. This shows why a map can help with revisions as well as first drafts.

Once the manual plan is useful, software may be able to manage the handoffs, save progress, or prevent a step from proceeding without approval. Those features must be implemented and tested. A diagram or an instruction to pause does not itself create an enforced restriction.

Use the [process worksheet](#/lab/process) to plan an assignment of your own. Start with the smallest set of tasks that makes the work clearer. Add a step when you can explain what it contributes or what error it prevents.
