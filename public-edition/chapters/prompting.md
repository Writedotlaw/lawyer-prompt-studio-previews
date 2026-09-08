# Give the AI an assignment it can act on.
> A useful prompt explains what you need and why. It supplies the relevant material, identifies the limits, and describes a result you can review.
@nav Write a useful prompt

## Explain what the work is supposed to accomplish.

“Summarize this contract” leaves the purpose open. A client deciding whether to sign may need to understand obligations and practical risks. A lawyer preparing for a termination dispute may need a much narrower account of notice requirements, cure rights, and remedies. The same agreement calls for different work.

Begin with that distinction. Tell the system who will use the result and what decision it should support. Identify the materials it may use, including any document that changes another. Where it matters, give your current view so the tool can engage with your reasoning rather than start from an unspecified position.

Then describe what you need back. A source-linked comparison table may be easier to review than a finished recommendation. A set of questions may be more useful than a first draft. Choosing the form of the response is part of designing the assignment.

## Draw on the prompting principles that the task needs.

The workshop materials identify ten useful choices. They are worth understanding, but you do not have to turn every prompt into a ten-part form.

Start with **role and audience**, then supply the **context, materials, and goal**. A role should identify a useful perspective, such as a skeptical reviewer of the stated argument. Calling the model “the world's best lawyer” does not supply the missing facts or a standard for the answer.

Use **annotated examples** when you can show the result you have in mind. Request **options or critique** when you have a decision to examine. State the **required form of the response**, and give **follow-up feedback** about what needs to change. For larger work, identify **steps that need to happen in order**, especially where one result must be checked before another task uses it.

You can also ask the tool to **help clarify your instructions** before it starts. **Save and reuse** the useful parts, while updating matter-specific information. Finally, **describe the writing problems to avoid**: an opening that delays the point, repetitive lists, or confident language that exceeds the evidence. Those directions are more useful than a general demand for excellent prose.

## Explain what an example demonstrates.

A sample heading might work because it names the person who acted and explains why the action matters. A client email might begin with the decision the client needs, then develop the reason in an order the client can follow. Name that choice when you provide the example.

Without the explanation, “write like this” asks the model to decide which features to copy. It might imitate a phrase you barely noticed while missing the organization that made the sample useful. It might also import facts or legal propositions that belong only to the example.

```prompt
Use the sample to learn how the writer introduces the dispute: it identifies who acted, explains the concrete conduct, and connects that conduct to the question the reader needs answered. Apply that approach to my passage. Do not copy the sample's facts, legal propositions, or distinctive phrases. Preserve every material qualification in my passage.
```

Examples can teach analysis as well as style. You might show how a strong paragraph connects particular facts to a rule, then ask the system to identify where your draft leaves that connection unexplained. Be precise about what the example is evidence of. It demonstrates a technique; it does not establish the law of the new matter.

## Prepare a prompt for something you understand.

Use the builder below with a fictional task or non-sensitive description. The fields help you explain the assignment, and the assembled prompt updates as you write. Loading an example shows the intended level of detail; it does not generate an answer.

Before copying the prompt into an approved AI tool, read it as an assignment to someone new to the matter. Are the important sources identified? Is there an unresolved choice you should make first? Have you asked for a result you will actually have time to review? Replace the remaining placeholders and supply the permitted documents in the tool itself.

{{widget:promptbuilder}}

## Review the proposed approach before substantial work begins.

For a larger assignment, ask the system to describe its plan before drafting. This gives you an early opportunity to correct a mistaken assumption about the goal or a missing source.

```prompt
Before you perform this assignment, explain how you understand the task. Identify material information that is missing or ambiguous, and propose a manageable approach using the permitted sources. Tell me which decisions you need me to make before proceeding. Wait for my response before drafting.
```

Review the plan against your own understanding. A tidy sequence can still be aimed at the wrong question. Once the plan fits, begin with the first useful task and check its result before moving forward. The next chapter shows how to make that sequence visible in a workflow map.
