Title: How to deal with Word Files in Git Systems
Date: 2016-02-26 10:20
Category: Agile
Tags: Git, Word, Versioning, Agile, DOC, DOCX
Slug: word-files-with-git
Author: Jonathan DEKHTIAR
Headline: Setting up a diff tool to manipulate Word Files : Rakali.

# How to deal with Word Files in Git Systems
### Setting up a diff tool to manipulate Word Files : Rakali.

***

I'd like first of all to acknowledge [Martin Fenner](http://blog.martinfenner.org/about.html){:target="\_blank"} for the method and the development.  
You can find extended blog post about this here : [link](http://blog.martinfenner.org/2014/08/25/using-microsoft-word-with-git/){:target="\_blank"}

So let’s get to businesss !

### Prerequisites

In order to be able to parse *doc* and *docx* file in Git you will need to install the following tools.


#### 1. If it’s not done yet, you should install **git**:
Click on this link to download and install: [**git-scm.com**](https://git-scm.com/downloads){:target="\_blank"}

#### 2. For the next phase of the tutorial, you will need to install **ruby**:

##### 2.1. Debian or Ubuntu:
```shell
sudo apt-get install ruby-full
```

##### 2.2. CentOS, Fedora, or RHEL:
```shell
sudo yum install ruby
```

##### 2.3. Mac OS X :

###### 2.3.1 Install Homebrew:
Click on this link to download and install: [**brew.sh**](http://brew.sh/){:target="\_blank"}    
###### 2.3.2 Then Install Ruby:
```shell
brew install ruby
```


#### 3.  Then install Rakali:
You may find all the information you need on the official [Github Repository](https://github.com/rakali/rakali.rb){:target="\_blank"}
```bash
gem install rakali
```

#### 4.  Create two files in your git project’s root folder :

##### 4.1. Create, at the git project root folder, the file: **".gitattributes"**

```dockerfile
# .gitattributes file in root folder of your git project
*.docx diff=pandoc
*.doc diff=pandoc
```

##### 4.2. Create, at the git project root folder, the file:  **".gitconfig"**

```dockerfile
# .gitconfig file in your home folder
[diff "pandoc"] #we declare the diff tool
textconv=pandoc --to=markdown
prompt = false
[alias]
wdiff = diff --word-diff=color --unified=1
```

#### 5.  Commit the two files and you’re done. Enjoy !
