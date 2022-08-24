#!/bin/ksh

export FILEPRFX=$1
if [ ! "${FILEPRFX}" ] ; then
   echo "Need file pattern."
   exit 89
fi

echo 
echo ${FILEPRFX}
echo 

fcnt=`aws s3 ls ${DATPROD_S3_BUCKET} --recursive | grep ${FILEPRFX} | wc -l`
if [ $fcnt == 0 ]; then
   echo "no files found, exit"
   exit 0
fi

echo "$fcnt files selected to remove:"
aws s3 ls ${DATPROD_S3_BUCKET} --recursive | grep ${FILEPRFX} | sort
echo 
echo "Continue? (y/n)"
read answer
echo 

if [[ $answer == "n" || $answer == "N" ]]; then
   echo "No, exit"
   exit 0
elif [[ $answer == "y" || $answer == "Y" ]]; then
   echo "Yes, continue"
else
   echo "Invalid choice, exit"
   exit 0
fi

#aws s3 rm ${DATPROD_S3_BUCKET} --recursive --include ${FILEPRFX}

exit 0



