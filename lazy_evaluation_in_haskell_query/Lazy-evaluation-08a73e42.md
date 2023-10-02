# Lazy evaluation

<div><div>
	<h3>From Wikipedia, the free encyclopedia</h3>
	<p>Jump to: <a href="#column-one">navigation</a>, <a href="#searchInput">search</a></p>	
	<table>
<tbody><tr>
<th><a href="/web/20060923094843/http://en.wikipedia.org/wiki/Computer_programming">Programming</a><br />
evaluation</th>
</tr>
<tr>
<td>
<p><a href="/web/20060923094843/http://en.wikipedia.org/wiki/Eager_evaluation">Eager</a><br />
<a href="/web/20060923094843/http://en.wikipedia.org/wiki/Evaluation_function">Function</a><br />
<strong>Lazy</strong><br />
<a href="/web/20060923094843/http://en.wikipedia.org/wiki/Minimal_evaluation">Minimal</a><br />
<a href="/web/20060923094843/http://en.wikipedia.org/wiki/Partial_evaluation">Partial</a><br />
<a href="/web/20060923094843/http://en.wikipedia.org/wiki/Remote_evaluation">Remote</a><br />
<a href="/web/20060923094843/http://en.wikipedia.org/wiki/Evaluation_strategy">Strategy</a></p>
</td>
</tr>
</tbody></table>
<p>In <a href="/web/20060923094843/http://en.wikipedia.org/wiki/Computer_programming">computer programming</a>, <b>lazy evaluation</b> is a technique that attempts to delay computation of expressions until the results of the computation are known to be needed. It has two related, yet different, meanings that could be described as <i>delayed evaluation</i> and <i>minimal evaluation</i>.</p>
<p>The benefits of lazy evaluation include: performance increases due to avoiding unnecessary calculations, avoiding error conditions in the evaluation of compound expressions, the ability to construct infinite <a href="/web/20060923094843/http://en.wikipedia.org/wiki/Data_structure">data structures</a>, and the ability to define <a href="/web/20060923094843/http://en.wikipedia.org/wiki/Control_structure">control structures</a> as regular functions rather than built-in primitives.</p>
<p>Languages that use lazy evaluation can be further subdivided into those that use a call-by-name <a href="/web/20060923094843/http://en.wikipedia.org/wiki/Evaluation_strategy">evaluation strategy</a> and those that use call-by-need. Most realistic lazy languages, such as <a href="/web/20060923094843/http://en.wikipedia.org/wiki/Haskell_programming_language">Haskell</a>, use call-by-need for performance reasons, but theoretical presentations of lazy evaluation often use call-by-name for simplicity.</p>
<p>The opposite of lazy evaluation is <a href="/web/20060923094843/http://en.wikipedia.org/wiki/Eager_evaluation">eager evaluation</a>, also known as <i><a href="/web/20060923094843/http://en.wikipedia.org/wiki/Evaluation_strategy#Strict_evaluation">strict evaluation</a></i>. Eager evaluation is the evaluation behavior used in most <a href="/web/20060923094843/http://en.wikipedia.org/wiki/Programming_languages">programming languages</a>.</p>
<div>
<p>
</p><h2>Contents</h2>
<p></p>
<ul>
<li><a href="#Compound_Expressions">1 Compound Expressions</a></li>
<li><a href="#Evading_error_conditions">2 Evading error conditions</a></li>
<li><a href="#Delayed_evaluation">3 Delayed evaluation</a></li>

