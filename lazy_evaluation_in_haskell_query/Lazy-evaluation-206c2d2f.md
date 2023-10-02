# Lazy evaluation

<div><div><p><b>Lazy evaluation</b> is a method to evaluate a Haskell program. It means that expressions are not evaluated when they are bound to variables, but their evaluation is <b>deferred</b> until their results are needed by other computations. In consequence, arguments are not evaluated before they are passed to a function, but only when their values are actually used.
</p><p>Technically, lazy evaluation means <a href="http://en.wikipedia.org/wiki/Evaluation_strategy#Call_by_name">call-by-name</a> plus <a href="/Sharing">Sharing</a>. A kind of opposite is <a href="/Eager_evaluation">eager evaluation</a>.
</p><p>Lazy evaluation is part of operational semantics, i.e. <i>how</i> a Haskell program is evaluated. The counterpart in denotational semantics, i.e. <i>what</i> a Haskell program computes, is called <a href="/Non-strict_semantics">Non-strict semantics</a>. This semantics allows one to bypass undefined values (e.g. results of infinite loops) and in this way it also allows one to process formally infinite data.
</p><p>While lazy evaluation has many advantages, its main drawback is that memory usage becomes hard to predict. The thing is that while two expressions, like <code>2+2 :: Int</code> and <code>4 :: Int</code>, may denote the same value 4, they may have very different sizes and hence use different amounts of memory.
</p><p>An extreme example would be the infinite list
<code>1 : 1 : 1 …</code> and the expression <code>let x = 1:x in x</code>. The latter is represented as a cyclic graph, and takes only finite memory, but its denotation is the former infinite list.
</p>
<h2>See also</h2>
<ul><li><a href="/Lazy_vs._non-strict">Lazy vs. non-strict</a></li>
<li><a href="https://hackhands.com/guide-lazy-evaluation-haskell/">The Incomplete Guide to Lazy Evaluation</a> – A series of tutorials on lazy evaluation: How it works, how it makes code more modular, how it relates to non-strict semantics, and other things.</li>
<li><a href="http://alpmestan.com/posts/2013-10-02-oh-my-laziness.html">Oh my laziness!</a> – An introduction to laziness and strictness in Haskell.</li></ul>
</div>

## Related Links
[[Understanding-Lazy-Evaluation-in-Haskell-18dad963]]
[[Lazy-evaluation---Wikipedia-8fc83770]]