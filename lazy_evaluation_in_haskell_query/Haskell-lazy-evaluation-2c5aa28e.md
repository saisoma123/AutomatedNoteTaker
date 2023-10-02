# Haskell lazy evaluation

<div><div>
 
<div>
 
 
<div>
 
 <div>
 
<p>If I call the following Haskell code</p>
<pre><code>find_first_occurrence :: (Eq a) =&gt; a -&gt; [a] -&gt; Int
find_first_occurrence elem list = (snd . head) [x | x &lt;- zip list [0..], fst x == elem]
</code></pre>
<p>with the arguments</p>
<pre><code>'X' "abcdXkjdkljklfjdlfksjdljjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj"
</code></pre>
<p>how much of the zipped list <code>[('a',0), ('b',1), ]</code> is going to be built?</p>
<p>UPDATE:</p>
<p>I tried to run</p>
<pre><code>find_first_occurrence 10 [1..]
</code></pre>
<p>and returns <code>9</code> almost instantly, so I guess it does use lazy evaluation at least for simple cases? The answer is also computed "instantly" when I run</p>
<pre><code>let f n = 100 - n
find_first_occurrence 10 (map f [1..])
</code></pre>
 </div>
 
 <div>
 <p>
 asked Mar 14, 2012 at 12:27
 </p>
 <div>
 <a href="/users/59557/quant-dev"><p></p></a>
 </div>
 <div>
 <p><a href="/users/59557/quant-dev">quant_dev</a>quant_dev</p><p>6,1031 gold badge34 silver badges56 bronze badges
 </p>
 </div>
</div>
 
</div>
 <p>11</p>
 </div>
 <div>
 
 
<div>
 
 <div>
<p>Short answer: it will be built only up to the element you're searching for. This means that only in the worst case you'll need to build the whole list, that is when no element satisfies the conditions.</p>
<p>Long answer: let me explain why with a pair of examples:</p>
<pre><code>ghci&gt; head [a | (a,b) &lt;- zip [1..] [1..], a &gt; 10]
11
</code></pre>
<p>In this case, zip should produce an infinite list, however the laziness enables Haskell to build it only up to <code>(11,11)</code>: as you can see, the execution does not diverge but actually gives us the correct answer.</p>
<p>Now, let me consider another issue:</p>
<pre><code>ghci&gt; find_first_occurrence 1 [0, 0, 1 `div` 0, 1]
*** Exception: divide by zero
ghci&gt; find_first_occurrence 1 [0, 1, 1 `div` 0, 0]
1
it :: Int
(0.02 secs, 1577136 bytes)
</code></pre>
<p>Since the whole zipped list is not built, haskell obviously will not even evaluate each expression occurring in the list, so when the element is before <code>div 1 0</code>, the function is correctly evaluated without raising exceptions: the division by zero did not occur.</p>
 </div>
 <div>
 <p>
 answered Mar 14, 2012 at 13:25
 </p>
 <div>
 <a href="/users/898400/riccardo-t"><p></p></a>
 </div>
 <div>
 <p><a href="/users/898400/riccardo-t">Riccardo T.</a>Riccardo T.</p><p>8,8075 gold badges36 silver badges78 bronze badges
 </p>
 </div>
</div>
 
</div>
 
<div>
 
 
<div>
 
 <div>
<p>All of it.</p>
<

