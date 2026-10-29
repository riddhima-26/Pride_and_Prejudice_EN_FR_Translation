# Translation samples (first 25 test sentences, greedy decoding)

### 1. Miss Bennet was the only creature who could suppose there might be any extenuating circumstances in the case, unknown to the society of Hertfordshire; her mild and steady candour always pleaded for allowances, and urged the possibility of mistakes--but by everybody else Mr. Darcy was condemned as the worst of men.

- **Reference:** Dans sa candeur charitable, elle plaidait toujours les circonstances atténuantes, et alléguait la possibilité d'une erreur, mais tous les autres s'accordaient pour condamner Mr. Darcy et le déclarer le plus méprisable des hommes.
- **Transformer (from scratch):** Bennet se mit a la voiture de la voiture de la maison et la voiture de la voiture de la voiture de la voiture de sa sour en meme meme meme meme meme meme meme meme meme meme pour lui faire une grande grande grande grande grande grande grande grande grande grande grande grande grande grande grande grande grande grande grande grande grande partie de Mr.
- **mT5-small (fine-tuned):** Miss Bennet était la seule personne qui avait supposé que cette situation était assez difficile a l'esprit de Hertfordshire, mais a tous les autres, Mr. Darcy était assez épris de l'impossibilité de faire a faire des corrections, mais a tous les autres, Mr.
- **Llama-3.2-1B (3-shot prompting):** La belle Miss Bennet était la seule créature qui pouvait supposer qu'il y avait des circonstances extenuantes dans le cas, inconnues à la société de Hertfordshire ; son candour doux et constante toujours plaide pour des allowances et pour l'idée de fautes, mais tout le monde la condamne comme l'homme le plus méchant.
- **Llama-3.2-1B (LoRA fine-tuned):** Miss Bennet, seule, pouvait supposer que les circonstances extenuantes de la situation ne savaient pas a Hertfordshire, et elle s'efforçait de prouver que les erreurs étaient possibles, mais les autres ne la voyaient pas ainsi.
- **Gemma-3-1B (3-shot prompting):** Miss Bennet était la seule créature qui pouvait supposer qu’il y avait des circonstances atténuantes dans le cas, inconnues de la société de Hertfordshire ; sa douce et stable courage plaida toujours pour des excuses, et encourageait la possibilité de fautes – mais par tous les autres, M. Darcy était condamné comme le pire d’entre les hommes.
- **Gemma-3-1B (LoRA fine-tuned):** Miss Bennet, seule dans cette société, pouvait imaginer des circonstances extraordinaires, inconnues de la cour de Hertfordshire. Son calme et sa douceur, toujours prônant les excuses, l'avaient toujours encouragée a croire que les erreurs pouvaient être des causes de ce qui se passait.

### 2. Mrs. Gardiner went away in all the perplexity about Elizabeth and her Derbyshire friend that had attended her from that part of the world.

- **Reference:** Mrs. Gardiner repartait non moins intriguée au sujet d'Elizabeth et de son ami de Pemberley qu'elle l'avait été en quittant le Derbyshire.
- **Transformer (from scratch):** Gardiner et sa sour se mit a Elizabeth et la conversation de sa sour et la conversation de sa sour et la conversation se mit a Elizabeth :
- **mT5-small (fine-tuned):** Mrs. Gardiner se dirigea vers toute la petite société de Elizabeth et sa Derbyshire dont l'avait été venue a l'univers.
- **Llama-3.2-1B (3-shot prompting):** Mme. Gardiner s'en alla dans l'incertitude sur Elizabeth et son ami de Derbyshire de cette partie du monde.
- **Llama-3.2-1B (LoRA fine-tuned):** Mrs. Gardiner s'en alla tout en perplexité sur Elizabeth et son ami de Derbyshire qui l'avait accompagnée de ce côté de la terre.
- **Gemma-3-1B (3-shot prompting):** Madame Gardiner s’est enfilée et s’est perdue dans la perplexité concernant Elizabeth et sa voisine de Derbyshire qui l’avait suivie de ce coin du monde.
- **Gemma-3-1B (LoRA fine-tuned):** Mrs. Gardiner quitta la maison en pleine perplexité sur Elizabeth et sa nouvelle amie de Derbyshire qui l'avait suivie de cette région.

### 3. Jane then took it from her pocket-book, and gave it to Elizabeth.

- **Reference:** Et Jane la prenant dans son portefeuille la tendit a Elizabeth.
- **Transformer (from scratch):** Jane se mit a sa mere et sa mere de son frere et sa mere.
- **mT5-small (fine-tuned):** Jane s'en leva de sa bibliotheque et lui avait donné la lettre a Elizabeth.
- **Llama-3.2-1B (3-shot prompting):** Jane prit ensuite le papier de sa pochette, et le remit à Elizabeth.
- **Llama-3.2-1B (LoRA fine-tuned):** Jane en sortit un morceau de papier et le lui donna a Elizabeth.
- **Gemma-3-1B (3-shot prompting):** Elle prit alors le livre de sa poche et le tendit à Elizabeth.
- **Gemma-3-1B (LoRA fine-tuned):** Jane prit le livre de sa poche et le tendit a Elizabeth.

### 4. This is my advice.

- **Reference:** Collins, il faut vous marier.
- **Transformer (from scratch):** C'est mon cher cher
- **mT5-small (fine-tuned):** Cette aide m'a fait a vous adresser ma conseil.
- **Llama-3.2-1B (3-shot prompting):** C'est ma recommandation.
- **Llama-3.2-1B (LoRA fine-tuned):** C'est ma recommandation.
- **Gemma-3-1B (3-shot prompting):** C’est mon conseil.
- **Gemma-3-1B (LoRA fine-tuned):** C'est mon conseil.

### 5. Elizabeth went away with her head full of him.

- **Reference:** Elizabeth partit l'esprit rempli de Mr. Wickham.
- **Transformer (from scratch):** Elizabeth se mit a sa sour avec une grande grande grande grande grande.
- **mT5-small (fine-tuned):** Elizabeth se dirigea vers lui.
- **Llama-3.2-1B (3-shot prompting):** Elisabeth s'en alla avec la tête pleine de lui.
- **Llama-3.2-1B (LoRA fine-tuned):** Elizabeth s'en alla avec son esprit a son amant.
- **Gemma-3-1B (3-shot prompting):** Elizabeth s’en alla avec sa tête remplie de lui.
- **Gemma-3-1B (LoRA fine-tuned):** Elizabeth quitta le jardin avec le cœur rempli de lui.

### 6. "When I wrote that letter," replied Darcy, "I believed myself perfectly calm and cool, but I am since convinced that it was written in a dreadful bitterness of spirit."

- **Reference:** – En écrivant cette lettre, reprit Darcy, je m'imaginais etre calme et froid ; mais je me rends compte maintenant que je l'ai écrite le cour plein d'une affreuse amertume.
- **Transformer (from scratch):** – Miss Bingley a fait fait de ce que je suis sure que je suis heureux et je suis sure que je suis sure que je suis heureux.
- **mT5-small (fine-tuned):** – Quand je écris ce lettre, répliqua Darcy, je crois que c'est une bonne humeur et une émotion agréable.
- **Llama-3.2-1B (3-shot prompting):** Quand j'ai écrit cette lettre," répondit Darcy, "je pensais être parfaitement calme et cool, mais depuis je suis convaincu qu'elle était écrite dans une bonté de cœur dévorante.
- **Llama-3.2-1B (LoRA fine-tuned):** – Quand j'ai écrit cette lettre, j'avais pensé que je me trouvais calme et cool, mais depuis j'ai compris que c'était écrit avec une colère qui m'a fait perdre tout le plaisir de la rédaction.
- **Gemma-3-1B (3-shot prompting):** – Quand j'ai écrit cette lettre, je pensais être parfaitement calme et froid, mais je suis depuis convaincu que c’était écrit avec une terrible bitterness d’esprit.
- **Gemma-3-1B (LoRA fine-tuned):** – Quand j'ai écrit cette lettre, répondit Darcy, je croyais être parfaitement calme et froid, mais depuis, je suis convaincu que c'était écrit avec une terrible amertume de l'esprit.

### 7. Nor did he seem much more at ease; when he spoke, his accent had none of its usual sedateness; and he repeated his inquiries as to the time of her having left Longbourn, and of her having stayed in Derbyshire, so often, and in so hurried a way, as plainly spoke the distraction of his thoughts.

- **Reference:** Darcy lui-meme ne semblait guere plus a l'aise. Sa voix n'avait pas sa fermeté habituelle et la façon dont, a plusieurs reprises, il la questionna sur l'époque ou elle avait quitté Longbourn et sur son séjour en Derbyshire, marquait clairement le trouble de son esprit.
- **Transformer (from scratch):** Les jeunes filles se mit a peine qu'il avait été plus de son frere et les deux jeunes filles en avait été a sa sour et ses filles en avait été moins moins de son mari et la voiture de son mariant a sa sour et la famille ne put s'empecher de son frere et ses manieres et la voiture.
- **mT5-small (fine-tuned):** Il n'avait pas été plus agréable, quand il parlait, il s'écria a son accent a l'heure de venir a Longbourn et de l'autre fois, et, a l'heure de l'heure de l'avoir quitté Longbourn, il s'adressa a l'heure de l'heure de l'avoir quitté Longbourn, autant que l'heure de son séjour a Longbourn, autant que de l
- **Llama-3.2-1B (3-shot prompting):** Il ne semblait pas beaucoup plus à l'aise ; lorsqu'il parlait, son accent n'avait plus de son habituelle élégance ; et il répétait ses questions sur le temps où elle avait quitté Netherfield et sur son séjour à Derbyshire, de manière si fréquente et si rapide, qu'il éclatait de distraction.
- **Llama-3.2-1B (LoRA fine-tuned):** Il ne semblait plus aussi a l'aise, quand il parlait, et ses accents avaient perdu leur élégance habituelle ; il répétait ses questions sur le temps qu'il avait passé a Longbourn et sur la durée de sa séjour a Derbyshire, et il les répétait avec une agitation qui montrait le désespoir de son esprit.
- **Gemma-3-1B (3-shot prompting):** Il ne semblait pas beaucoup plus à l’aise ; quand il parlait, son accent n’avait pas de sa douceur habituelle ; et il répétait ses questions sur le moment où elle avait quitté Longbourn et sur le fait qu’elle était restée dans le Derbyshire, si souvent, et d’une manière si précipitée, que le distraitement de ses pensées était évident.
- **Gemma-3-1B (LoRA fine-tuned):** Il ne semblait pas plus détendu, quand il parla, son accent n'était pas aussi paisible que d'habitude, et il répéta les questions sur le temps où elle avait quitté Longbourn et sur le temps qu'elle passait a Derbyshire, avec une rapidité qui lui donnait l'impression d'être occupé par ses pensées.

### 8. "No, indeed, I do not wish to avoid the walk.

- **Reference:** – Nullement ; je ne crains pas la marche.
- **Transformer (from scratch):** – Non, je ne vous en voir a la conversation.
- **mT5-small (fine-tuned):** – Non, vraiment, je ne puis vous voir a l'éloigner.
- **Llama-3.2-1B (3-shot prompting):** Non, je ne veux pas m'échapper à la promenade.
- **Llama-3.2-1B (LoRA fine-tuned):** – Non, je ne veux pas m'échapper a ce promenade.
- **Gemma-3-1B (3-shot prompting):** Non, bien sûr, je ne veux pas éviter la marche.
- **Gemma-3-1B (LoRA fine-tuned):** – Non, je ne veux pas me faire de mal, je veux bien marcher.

### 9. She has been doing everything in her power by thinking and talking on the subject, to give greater--what shall I call it? susceptibility to her feelings; which are naturally lively enough. And we all know that Wickham has every charm of person and address that can captivate a woman."

- **Reference:** Bref elle a fait tout ce qu'elle pouvait – comment dirai-je, – pour donner encore plus de force a des penchants déja si accusés. Et vous savez comme moi que Wickham, par la séduction de ses manieres et de sa personne, a tout ce qu'il faut pour tourner une tete de jeune fille.
- **Transformer (from scratch):** Elle a été été pour lui dit que nous avons avons eu le plus de son mari et que nous a une telle telle telle telle telle telle telle telle telle telle telle telle telle telle telle telle telle telle telle telle telle telle telle telle telle telle qu'il est un peu de la plus tôt.
- **mT5-small (fine-tuned):** Elle a été assez loin de penser a ce sujet : l'intelligence de Wickham a toutes les sentiments qui sont assez naturels et a l'adresse de l'homme qui a été pleinement agréable.
- **Llama-3.2-1B (3-shot prompting):** Elle a fait tout ce qu'elle a pu pour penser et parler sur le sujet, pour rendre plus susceptible à ses émotions ; ce qui est naturellement suffisant. Et nous savons que Wickham a tout ce dont elle a besoin pour captiver une femme.
- **Llama-3.2-1B (LoRA fine-tuned):** Elle a fait tout ce qu'elle pouvait pour donner plus de sympathie a ses sentiments, qui sont naturellement vivaces. Nous savons que Wickham a tout ce qui peut captiver une femme.
- **Gemma-3-1B (3-shot prompting):** Elle a fait tout ce qu’elle pouvait en pensant et en parlant sur le sujet, pour donner une plus grande – qu’est-ce qu’elle appelle ? susceptibilité à ses sentiments ; qui sont naturellement assez vivaces. Et nous savons tous que Wickham a chaque charme d’homme et adresse qui peuvent captiver une femme.
- **Gemma-3-1B (LoRA fine-tuned):** Elle a fait tout ce qu'elle pouvait pour donner a ses sentiments une plus grande réceptivité, et nous savons tous que Wickham a le charme de la personne et de l'adresse qui peuvent captiver une femme.

### 10. I talked to her repeatedly in the most serious manner, representing to her all the wickedness of what she had done, and all the unhappiness she had brought on her family.

- **Reference:** Je lui ai parlé tres sérieusement a plusieurs reprises, lui montrant la gravité de sa faute et le chagrin qu'elle avait causé a sa famille.
- **Transformer (from scratch):** Je suis sure que la lettre de son mari en avait été le plus tôt, et la porte en avait été si elle avait été trompée et de son mariant a son mari et la voiture de son mari a son mari et la voiture de son mariant a son frere et la voiture.
- **mT5-small (fine-tuned):** Je suis ainsi a l'instant de l'avoir fait, et a toute la crainte qu'elle avait fait, elle avait apportée a sa famille.
- **Llama-3.2-1B (3-shot prompting):** J'ai parlé à elle de manière la plus sérieuse, représentant à elle tout le mal qu'elle avait fait et tout le chagrin qu'elle avait causé à sa famille.
- **Llama-3.2-1B (LoRA fine-tuned):** Je lui parlai plusieurs fois avec une gravité sérieuse, représentant a elle tout le mal qu'elle avait fait et tout le mal qu'elle avait causé a sa famille.
- **Gemma-3-1B (3-shot prompting):** J’ai parlé à elle à plusieurs reprises avec la plus grande seriosité, en représentant à elle toutes les méchancetésques choses qu’elle avait faites et tous les malheurs qu’elle avait causés à sa famille.
- **Gemma-3-1B (LoRA fine-tuned):** J'ai parlé a elle de la plus grande tristesse que j'avais pu imaginer, et de la souffrance qu'elle avait causée a sa famille.

### 11. "The letter, perhaps, began in bitterness, but it did not end so. The adieu is charity itself.

- **Reference:** – Peut-etre commençait-elle dans l'amertume, mais elle se terminait par un adieu plein de charité.
- **Transformer (from scratch):** – Le colonel Forster ne pouvait pas a la lettre : mais il est une lettre de Mr.
- **mT5-small (fine-tuned):** – La lettre, peut-etre, s'éloignait a la crainte, mais il ne s'en était pas a l'instant.
- **Llama-3.2-1B (3-shot prompting):** La lettre, peut-être, a commencé dans la colère, mais elle n'a pas fini. L'adieu est en soi la charité.
- **Llama-3.2-1B (LoRA fine-tuned):** – Le billet, peut-etre, a commencé avec une colère, mais il n'a pas fini.
- **Gemma-3-1B (3-shot prompting):** – L’ lettre, peut-être, avait commencé par la rancœur, mais elle ne s’est pas terminée ainsi. L’adieu est lui-même de la charité.
- **Gemma-3-1B (LoRA fine-tuned):** – La lettre, peut-etre, a commencé avec un sentiment de méchanceté, mais elle n'a pas fini par s'en soucier.

### 12. Her prudent mother, occupied by the same ideas, forbore to invite him to sit by herself.

- **Reference:** Il parut hésiter tout d'abord ; mais Jane, par hasard, regardait de son côté en souriant.
- **Transformer (from scratch):** Son pere et la voiture a la voiture de se marier dans la voiture de lui faire a la voiture de leur pere et la voiture.
- **mT5-small (fine-tuned):** Elle s'occupa de telles idées, et, a l'heure des autres, s'empecher de l'inviter a s'installer a son côté.
- **Llama-3.2-1B (3-shot prompting):** Sa mère prudente, occupée par les mêmes idées, ne voulait pas l'inviter à s'asseoir seule.
- **Llama-3.2-1B (LoRA fine-tuned):** Sa mere prudente, occupée a ces idées, ne lui a pas permis de s'asseoir seule.
- **Gemma-3-1B (3-shot prompting):** Sa mère prudente, occupée des mêmes idées, s’abstrait d’inviter son fils à s’asseoir seul.
- **Gemma-3-1B (LoRA fine-tuned):** Sa maman prudente, occupée de la même idée, ne l'invita pas a s'asseoir seule.

### 13. Everything nourishes what is strong already.

- **Reference:** Tout fortifie ce qui est déja fort.
- **Transformer (from scratch):** – Le colonel Forster est vous etes ?
- **mT5-small (fine-tuned):** Tout n'a pas l'air assez élevée.
- **Llama-3.2-1B (3-shot prompting):** Tout nourrit ce qui est déjà fort.
- **Llama-3.2-1B (LoRA fine-tuned):** Tout nourrit ce qui est fort.
- **Gemma-3-1B (3-shot prompting):** Tout nourrit ce qui est déjà fort.
- **Gemma-3-1B (LoRA fine-tuned):** Tout nourrit ce qui est déjà fort.

### 14. That such a consequence as _this_ could ensue, you may easily believe, was far enough from my thoughts."

- **Reference:** Vous devinez combien j'étais loin de penser que mon silence put causer une telle catastrophe !
- **Transformer (from scratch):** « C'est une fois pour vous voir qu'il est trop trop trop de vous en en en en en en en en en faveur.
- **mT5-small (fine-tuned):** Cette consolation vous semblerait difficile de vous croire, et vous pouvez croire que cette idée était assez difficile de mes pensées.
- **Llama-3.2-1B (3-shot prompting):** Ceci est une conséquence si évidente qu'elle vous fait facilement croire.
- **Llama-3.2-1B (LoRA fine-tuned):** C'est ainsi que vous pouvez le croire, car je n'avais pas l'intention de me laisser emporter par une telle idée.
- **Gemma-3-1B (3-shot prompting):** – Ce résultat aussi éloquent, vous pouvez facilement croire, était bien loin de mes pensées.
- **Gemma-3-1B (LoRA fine-tuned):** Vous pouvez facilement croire que cette conséquence, si elle devait arriver, était bien loin de mes pensées.

### 15. Before they were separated by the conclusion of the play, she had the unexpected happiness of an invitation to accompany her uncle and aunt in a tour of pleasure which they proposed taking in the summer.

- **Reference:** Avant la fin de la représentation, Elizabeth eut le plaisir tres inattendu de se voir inviter par son oncle et sa tante a les accompagner dans le voyage d'agrément qu'ils projetaient pour l'été suivant.
- **Transformer (from scratch):** A la voiture de la porte a la conversation de la voiture et la porte de la voiture de la voiture n'était pas a la voiture de la porte pour les deux ou elle se trouvait en dépit de la porte a la porte de la voiture de la maison.
- **mT5-small (fine-tuned):** Quand elles furent partis par la conclusion de la musique, elle avait l'espoir de faire une invitation a accompagner son oncle et sa tante dans une tour de plaisir qui leur proposait a l'été dernier.
- **Llama-3.2-1B (3-shot prompting):** Avant qu'ils ne soient séparés par la fin du spectacle, elle avait la surprise d'une invitation pour accompagner son oncle et sa tante en une tour de plaisir qu'ils proposaient de prendre d'été.
- **Llama-3.2-1B (LoRA fine-tuned):** Avant qu'ils ne se séparente par la fin du spectacle, elle avait l'occasion d'etre invitée a accompagner son oncle et sa tante a une promenade de plaisir qu'ils proposaient de faire en été.
- **Gemma-3-1B (3-shot prompting):** Avant que la séparation ne soit imposée par la fin du spectacle, elle avait la surprise de l’invitation à accompagner son oncle et sa tante dans un voyage de plaisirs qu’ils lui proposèrent de faire en été.
- **Gemma-3-1B (LoRA fine-tuned):** Avant que le spectacle se termine, elle avait l'inattendu bonheur d'être invitée a accompagner son oncle et sa tante dans un voyage de plaisir qu'ils proposaient de faire en été.

### 16. "All this she must possess," added Darcy, "and to all this she must yet add something more substantial, in the improvement of her mind by extensive reading."

- **Reference:** – Et a tout ceci, ajouta Mr. Darcy, elle doit ajouter un avantage plus essentiel en cultivant son intelligence par de nombreuses lectures.
- **Transformer (from scratch):** – En vérité, répliqua Elizabeth, elle n'avait plus de se marier a son mari ; mais elle se marier a sa sour en disant : – elle n'avait pas de son mariant sa sour.
- **mT5-small (fine-tuned):** – Allons ce qu'elle doit avoir, ajouta Darcy, et elle doit ajouter un peu plus agréable dans le nouveau esprit de son esprit.
- **Llama-3.2-1B (3-shot prompting):** Chaque chose qu'elle doit posséder," dit Darcy, "et à chaque chose qu'elle doit encore ajouter, quelque chose de plus substantiel, grâce à la lecture approfondie de ses pensées.
- **Llama-3.2-1B (LoRA fine-tuned):** – Tout cela, ajouta Darcy, il lui faut encore quelque chose de plus substantiel, en matière de perfection de son esprit, grâce a la lecture.
- **Gemma-3-1B (3-shot prompting):** – Elle doit posséder tout cela, et elle doit encore ajouter quelque chose de plus substantiel à l’amélioration de son esprit par une lecture étendue.
- **Gemma-3-1B (LoRA fine-tuned):** – Tout cela, ajouta Darcy, elle doit en posséder, et elle doit encore ajouter quelque chose de plus important pour améliorer son esprit par la lecture.

### 17. "Well, well, and so Mr. Bingley is coming down, sister," (for Mrs. Phillips first brought her the news).

- **Reference:** – Alors, Mr. Bingley est donc sur le point de revenir, ma sour ? disait-elle a Mrs.
- **Transformer (from scratch):** – Eh bien, Mr. Bingley est une lettre de Mrs. Bennet, et Mrs. Bennet, qui est une grande grande grande grande partie de Mrs.
- **mT5-small (fine-tuned):** – Eh bien, bien, et si Mr. Bingley est arrivé, sour, car Mrs. Philips a l'occasion de venir a l'heure.
- **Llama-3.2-1B (3-shot prompting):** "Très bien, très bien, et voilà, sœur," (pour la mère Phillips a d'abord apporté la nouvelle).
- **Llama-3.2-1B (LoRA fine-tuned):** – Eh bien, et voila Mr. Bingley qui descend !
- **Gemma-3-1B (3-shot prompting):** – Ah, bien, bien, et donc Mr. Bingley arrive, sœur !
- **Gemma-3-1B (LoRA fine-tuned):** – Eh bien, eh bien, et Mr. Bingley est en train de descendre, ma mere.

### 18. If she heard me, it was by good luck, for I am sure she did not listen.

- **Reference:** Si elle m'a entendue, c'est une chance, car je suis certaine qu'elle ne m'a jamais écoutée.
- **Transformer (from scratch):** Si je suis sure qu'elle avait été été plus tardée que je ne vous avez pas en en en en en en pensant que je suis pas vous avez vu.
- **mT5-small (fine-tuned):** Si elle m'écoutait, il était assez bonheur, car je suis sure que c'est a la fois que j'en ai écouté.
- **Llama-3.2-1B (3-shot prompting):** Si elle me entendait, c'était par chance, car je suis sûr qu'elle ne l'écoute pas.
- **Llama-3.2-1B (LoRA fine-tuned):** Si elle m'entendait, c'était par la chance, car je suis sûr qu'elle ne l'écoute pas.
- **Gemma-3-1B (3-shot prompting):** Si elle m’entendait, c’était par chance, car je suis sûr qu’elle ne l’entendait pas.
- **Gemma-3-1B (LoRA fine-tuned):** Si elle avait entendu, c'était par chance, car je suis certain qu'elle n'a pas écouté.

### 19. "I should never have said Mrs. Collins was settled _near_ her family."

- **Reference:** Je ne trouve pas qu'elle soit établie a proximité de sa famille.
- **Transformer (from scratch):** – Je suis sure que Mrs. Bennet, dit Mrs. Bennet, en en en en en plus tarder.
- **mT5-small (fine-tuned):** – Je ne puis avoir dit Mrs. Collins a la famille de sa famille.
- **Llama-3.2-1B (3-shot prompting):** Je ne devrais jamais avoir dit qu'elle était assise à proximité de sa famille.
- **Llama-3.2-1B (LoRA fine-tuned):** – Je ne l'ai jamais dit que Mrs. Collins était a la maison de sa famille.
- **Gemma-3-1B (3-shot prompting):** – Je ne devrais jamais avoir dit que Mme. Collins était proche de sa famille.
- **Gemma-3-1B (LoRA fine-tuned):** – Je n'aurais jamais dit que Mrs. Collins était proche de sa famille.

### 20. In an hurried manner he immediately began an inquiry after her health, imputing his visit to a wish of hearing that she were better.

- **Reference:** Il se hâta tout d'abord de s'enquérir de sa santé, expliquant sa visite par le désir qu'il avait d'apprendre qu'elle se sentait mieux.
- **Transformer (from scratch):** A la fin, il avait eu le mariage de son frere et a sa sour a sa sour en avait été a sa sour sur le mariage de sa sour et a sa sour :
- **mT5-small (fine-tuned):** Il s'en aperçut a son état de santé, et, a l'heure du lendemain, il s'en aperçut a son hôte a un désir de voir qu'elle était mieux.
- **Llama-3.2-1B (3-shot prompting):** En un mouvement hasty, il commença aussitôt une enquête sur son état, imputant son visiteur à un désir de l'entendre dire qu'elle était mieux.
- **Llama-3.2-1B (LoRA fine-tuned):** Il commença tout de suite a demander l'état de sa santé, en supposant qu'il venait de la voir mieux.
- **Gemma-3-1B (3-shot prompting):** Il commença immédiatement une enquête sur sa santé, attribuant sa visite à un désir de savoir qu’elle étaient mieux.
- **Gemma-3-1B (LoRA fine-tuned):** Il s'enfonça immédiatement dans la question de sa santé, en insinuant qu'il avait visité pour entendre qu'elle était mieux.

### 21. "If you _will_ thank me," he replied, "let it be for yourself alone.

- **Reference:** – Si vous tenez a me remercier, répliqua Darcy, remerciez-moi pour vous seule.
- **Transformer (from scratch):** – Si vous vous vous vous vous avez été, je vous en vous avez été !
- **mT5-small (fine-tuned):** – Si vous vous remercie, répliqua-t-il, vous l'avez donné assez pour moi.
- **Llama-3.2-1B (3-shot prompting):** Si vous voulez m'apprécier, laissez cela être pour vous-même seul.
- **Llama-3.2-1B (LoRA fine-tuned):** – Si vous voulez m'apprécier, dit-il, laissez-moi vous en remercier.
- **Gemma-3-1B (3-shot prompting):** – Si tu me remercieras, laisse cela pour toi seul.
- **Gemma-3-1B (LoRA fine-tuned):** – Si vous me remerciez, je vous le dirai, dit-il, pour vous seul.

### 22. "Dearest Jane! who could have done less for her?

- **Reference:** – Cette chere Jane ! Qui donc n'en aurait fait autant pour elle ?
- **Transformer (from scratch):** – Oui, Jane ! Jane a Jane ?
- **mT5-small (fine-tuned):** – Jane ! qui avait fait plus de chose a elle ?
- **Llama-3.2-1B (3-shot prompting):** Mon amour, qui n'a pas fait que de la joie à ta vie.
- **Llama-3.2-1B (LoRA fine-tuned):** – Ma chere Jane, qui a pu faire autant de mal ?
- **Gemma-3-1B (3-shot prompting):** – Chère Jane ! Qui aurait pu faire moins pour elle ?
- **Gemma-3-1B (LoRA fine-tuned):** – Jane, qui aurait pu faire plus pour elle ?

### 23. "I am trying to make it out."

- **Reference:** J'essaye en ce moment de le comprendre.
- **Transformer (from scratch):** – Je suis sure que je suis a vous voir.
- **mT5-small (fine-tuned):** – Je suis contente de faire ce qu'il faut.
- **Llama-3.2-1B (3-shot prompting):** – Je cherche à le comprendre.
- **Llama-3.2-1B (LoRA fine-tuned):** – Je cherche a comprendre.
- **Gemma-3-1B (3-shot prompting):** – Je essaie de le voir.
- **Gemma-3-1B (LoRA fine-tuned):** – Je cherche a comprendre.

### 24. He walked away again immediately, and she was left to fret over her own want of presence of mind; Charlotte tried to console her:

- **Reference:** Il s'éloigna aussitôt, la laissant toute dépitée d'avoir montré si peu de présence d'esprit. Charlotte Lucas essaya de la réconforter :
- **Transformer (from scratch):** Il lui avait eu pour le plus de son pere et de son pere : – En effet, effet, effet, se mit a son pere et de son pere ?
- **mT5-small (fine-tuned):** Il se dirigea vers la voiture et elle se mit a s'empecher de s'entendre :
- **Llama-3.2-1B (3-shot prompting):** Il se détourna à nouveau immédiatement, et elle fut laissée à se soucier de sa propre manque de présence de conscience ; Charlotte essaya de la consoler.
- **Llama-3.2-1B (LoRA fine-tuned):** Il se détourna et elle fut laissée a se frotter sur sa propre absence de prudence. Charlotte essaya de la consoler.
- **Gemma-3-1B (3-shot prompting):** Il s’est éloigné à nouveau à nouveau, et elle fut laissée à se plaindre de son manque de présence d’esprit ; Charlotte tenta de la réconforter :
- **Gemma-3-1B (LoRA fine-tuned):** Il s'éloigna aussitôt et elle fut laissée a se plaindre de son manque de présence d'esprit.

### 25. "I know not, Miss Elizabeth," said he, "whether Mrs. Collins has yet expressed her sense of your kindness in coming to us; but I am very certain you will not leave the house without receiving her thanks for it.

- **Reference:** – Je ne sais, miss Elizabeth, si Mrs. Collins vous a déja dit combien votre visite l'avait touchée, mais je suis certain que vous ne quitterez pas cette maison sans recevoir ses remerciements.
- **Transformer (from scratch):** – Je ne vous ai pas de miss Bingley, mais je suis sure que vous en en en en en en pensant a vous en pensant a vous avez fait pour vous en en pensant a votre fille de vous en en en pensant a votre fille sans doute.
- **mT5-small (fine-tuned):** – Je ne sais pas, miss Elizabeth, si Mrs. Collins a exprimé sa bonté, mais je suis sure que vous ne vous l'avez pas exprimée a vous faire aucun plaisir a venir nous rendre a l'hôtel sans recevoir la bonne gratitude.
- **Llama-3.2-1B (3-shot prompting):** Je ne sais pas, mademoiselle Elizabeth, ce que Mme. Collins a dit à ce jour, en ce qui concerne votre gentillesse en venant nous voir ; mais je suis sûr que vous ne partirerez pas de cette maison sans recevoir ses remerciements.
- **Llama-3.2-1B (LoRA fine-tuned):** – Je ne sais pas, miss Elizabeth, dit Mr. Darcy, si Mrs. Collins a exprimé son appréciation de votre visite, mais je suis certaine que vous ne quitterez pas la maison sans recevoir les remerciements de Mrs.
- **Gemma-3-1B (3-shot prompting):** – Je ne sais pas, Madame Elizabeth, si Mme. Collins n’a pas encore exprimé sa gratitude pour notre accueil ; mais je suis certain que vous ne quitterez pas votre maison sans recevoir ses remerciements.
- **Gemma-3-1B (LoRA fine-tuned):** – Je ne sais pas, dit-il, si Mrs. Collins n'a pas encore exprimé sa gratitude pour votre visite, mais je suis certain que vous ne quitterez pas la maison sans lui exprimer votre reconnaissance.

