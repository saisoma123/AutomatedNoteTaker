# Lazy evaluation - Wikipedia

<div><div>
<p>In <a href="/wiki/Programming_language_theory">programming language theory</a>, <b>lazy evaluation</b>, or <b>call-by-need</b>,<sup><a href="#cite_note-1">[1]</a></sup> is an <a href="/wiki/Evaluation_strategy">evaluation strategy</a> which delays the evaluation of an <a href="/wiki/Expression_(computer_science)">expression</a> until its value is needed (<a href="/wiki/Non-strict_evaluation">non-strict evaluation</a>) and which also avoids repeated evaluations (<a href="/wiki/Sharing_(computer_science)">sharing</a>).<sup><a href="#cite_note-WattFindlay2004-2">[2]</a></sup><sup><a href="#cite_note-3">[3]</a></sup>
</p><p>The benefits of lazy evaluation include: 
</p>
<ul><li>The ability to define <a href="/wiki/Control_flow">control flow</a> (structures) as abstractions instead of <a href="/wiki/Language_primitive">primitives</a>.</li>
<li>The ability to define <a href="/wiki/Actual_infinity">potentially infinite</a> <a href="/wiki/Data_structure">data structures</a>. This allows for more straightforward implementation of some algorithms.</li>
<li>The ability to define partially-defined data structures where some elements are errors. This allows for rapid prototyping.</li></ul>
<p>Lazy evaluation is often combined with <a href="/wiki/Memoization">memoization</a>, as described in <a href="/wiki/Jon_Bentley_(computer_scientist)">Jon Bentley</a>'s <i>Writing Efficient Programs</i>.<sup><a href="#cite_note-4">[4]</a></sup> After a function's value is computed for that parameter or set of parameters, the result is stored in a <a href="/wiki/Lookup_table">lookup table</a> that is indexed by the values of those parameters; the next time the function is called, the table is consulted to determine whether the result for that combination of parameter values is already available. If so, the stored result is simply returned. If not, the function is evaluated and another entry is added to the lookup table for reuse.
</p><p>Lazy evaluation is difficult to combine with imperative features such as <a href="/wiki/Exception_handling">exception handling</a> and <a href="/wiki/Input/output">input/output</a>, because the order of operations becomes indeterminate. 
</p><p>The opposite of lazy evaluation is <a href="/wiki/Eager_evaluation">eager evaluation</a>, sometimes known as strict evaluation. Eager evaluation is the evaluation strategy employed in most<sup>[<i><a href="/wiki/Wikipedia:Manual_of_Style/Dates_and_numbers">quantify</a></i>]</sup> <a href="/wiki/Programming_language">programming languages</a>.
</p>
<h2>History[<a href="/w/index.php?title=Lazy_evaluation&amp;action=edit&amp;section=1">edit</a>]</h2>
<p>Lazy evaluation was introduced for <a href="/wiki/Lambda_calculus">lambda calculus</a> by Christopher Wadsworth<sup><a href="#cite_note-5">[5]</a></sup> and employed by the <a href="/wiki/Plessey_System_250">Plessey System 250</a> as a critical part of a Lambda-Calculus Meta-Machine, reducing the resolution overhead for access to objects in a capability-limited address space.<sup><a href="#cite_note-6">[6]</a></sup> For programming languages, it was independently introduced by Peter Henderson and <a href="/wiki/James_H._Morris">James H. Morris</a><sup><a href="#cite_note-7">[7]</a></sup> and by <a href="/wiki/Daniel_P._Friedman">Daniel P. Friedman</a> and David S. Wise.<sup><a href="#cite_

## Related Links
[[Lazy-evaluation-08a73e42]]
[[Lazy-evaluation-2a28c1c5]]