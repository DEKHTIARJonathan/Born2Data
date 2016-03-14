Title: How to deal with Word Files in Git Systems
Date: 2016-02-26 10:20
Category: Git, Word, Versioning, Agile
Tags: Git, Word, Versioning, Agile, DOC, DOCX
Slug: word-files-with-git
Author: Jonathan DEKHTIAR
Summary: Setting up a diff tool to manipulate Word Files : Rakali.


I'd like first of all to acknowledge [Martin Fenner](http://blog.martinfenner.org/about.html){:target="_blank"} for the method and the development.  
You can find extended blog post about this here : [link](http://blog.martinfenner.org/2014/08/25/using-microsoft-word-with-git/){:target="_blank"}

So let’s get to businesss:

**Here are the steps you will need to follow :**

1.  Install GIT, if it’s not done yet: [link](https://git-scm.com/downloads){:target="_blank"}

2.  Install RUBY:

    1.  Debian or Ubuntu:

            :::shell
            sudo apt-get install ruby-full

    2.  CentOS, Fedora, or RHEL:

		    :::shell
            sudo yum install ruby

    3.  Mac OS X :

        1.  Install Homebrew: [link](http://brew.sh/){:target="_blank"}

        2.  Then Install Ruby: 
		
		        :::shell
                brew install ruby

3.  Then install Rakali: [Github Repo](https://github.com/rakali/rakali.rb){:target="_blank"}

		:::shell
        gem install rakali

5.  Create two files in your git project’s root folder :

    1.  File: ".gitattributes"

            :::dockerfile
			# .gitattributes file in root folder of your git project
			*.docx diff=pandoc
			*.doc diff=pandoc
			
    2.  File: ".gitconfig"

            :::dockerfile
			# .gitconfig file in your home folder
			[diff "pandoc"] #we declare the diff tool
			textconv=pandoc --to=markdown
			prompt = false
			[alias]
			wdiff = diff --word-diff=color --unified=1

6.  Commit the two files and you’re done. Enjoy !