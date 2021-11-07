(defn questionCorrectionBot [question] 
   (-> question
       clojure.string/trim
       (str "?")
       (clojure.string/replace  #"," ", ")
       (clojure.string/replace  #"\s+," ",")
       (clojure.string/replace  #"\s+" " ")
       (clojure.string/replace  #"\?+" "?")
       (#(str (clojure.string/capitalize (subs % 0 1)) (subs % 1)))))