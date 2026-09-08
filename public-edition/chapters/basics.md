# Understand the tool well enough to direct it.
> You do not need an engineering background to use AI thoughtfully. You do need to distinguish what the model generates from what it retrieves, and a written instruction from a control the software actually enforces.
@nav How the tools work

## A generated answer is different from a source you have checked.

Artificial intelligence covers a broad range of systems. Some classify information or predict an outcome. Others generate content. This guide focuses on the language tools lawyers use to work with documents and ideas, which are built around large language models.

A language model learns patterns during training and uses them to generate a response. An application may also provide your documents, retrieve material from a database, or let the model use another tool. When you ask a legal question, the answer might therefore draw on several different kinds of information. Find out which ones were available for the particular response you are reviewing.

Suppose a tool gives you a case citation and a paragraph explaining its holding. The citation's appearance tells you little about whether the case exists or supports the proposition. Even when the case is real, the explanation might confuse the court's holding with a party's argument. The term **hallucination** is commonly used for false or invented content, but smaller distortions deserve the same attention. A summary that changes “the plaintiff alleges” to “the defendant did” has changed the facts you are being asked to rely on.

The practical habit is to connect important statements with their supporting material. Then read that material in context. Asking the tool to include citations makes this review easier; it does not perform the review for you.

## The model and the application have different jobs.

The model is one part of the product you use. The surrounding software determines what files it can read, whether it can search, and which actions it may take. Developers sometimes call that surrounding system a **harness**. Think of the model as an engine and the application as the rest of the car: the engine matters, but so do the controls and where the car can go.

Two products using the same underlying model may handle your work quite differently. One may search an approved collection of legal materials. Another may let you upload a contract but have no access to the amendment stored elsewhere. One may draft an email for review; another may have permission to send it.

When someone demonstrates a product, ask to see those details. Which documents supported the answer? What happens when a file cannot be read? Can the system send something before you approve it? Understanding the application gives you a better basis for evaluating the proposed use than the model's name alone.

## Keep an accurate record outside the conversation.

The **context window** is the information a model can consider while generating a response. Its capacity is measured in **tokens**, small units of text or other encoded input. A long conversation may be shortened or summarized to fit the available space. Product memory features work differently and should not be treated as a dependable record of every instruction or decision.

For a continuing matter, keep the current assignment and reviewed findings in a separate reference document. Imagine returning to a contract analysis after a new amendment arrives. The next session needs to know that the amendment now controls, which earlier conclusions require reconsideration, and which questions remain open. “Continue where we left off” may not supply any of that.

You can ask AI to prepare the reference document, but review it before using it again. Mark the difference between a suggestion the system made and a decision you approved. Otherwise, the saved summary can turn an unaccepted proposal into the starting assumption for the next session.

Context capacity is also separate from confidentiality. What a model can consider in a response does not tell you how long the provider retains your files or who can access them. Those questions require checking the actual service, account settings, and applicable terms.

## Learn the terms when they help you make a decision.

**Retrieval-augmented generation**, usually shortened to **RAG**, means the system retrieves material and uses it to help compose an answer. For legal work, that might mean finding opinions in a research database or provisions in uploaded agreements. You need to assess both stages: did it find the relevant material, and did it interpret that material correctly?

A **reasoning model** is designed to spend additional computation working through a problem before answering. That may help with a difficult assignment, but the label does not establish that its answer is right. Evaluate the work it returns.

An **agent** can pursue an assignment through a series of actions, such as searching for a source, reading it, and revising a draft. An **API** is a connection that lets one software system communicate with another. These terms become useful when you ask what a product can access and do. You do not need to memorize them before practicing with the guide; the glossary is available whenever a term gets in your way.

## Test the use you are considering.

A system can perform well on one task and poorly on a nearby one. A clear summary of a provision does not establish that it will find every exception across a collection of agreements. Nor does a successful demonstration establish how it handles an unreadable page or a missing document.

Start with material you understand and a result you can check. For a clause-comparison task, identify an important difference yourself, then see whether the system finds and explains it. Change the example so a necessary provision is missing. Does the response report the gap, or continue as though the documents were complete?

These small tests give you more useful information than asking the system whether it is good at legal analysis. Keep a record of what worked, what failed, and what you changed. You will return to that habit when we build more substantial workflows.
