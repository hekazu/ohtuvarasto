module Message where

printDefaultMessage :: IO ()
printDefaultMessage = printMessage "Hello, World!"

printMessage :: Show a => a -> IO ()
printMessage = print
