module Message where

printDefaultMessage :: IO ()
printDefaultMessage = printMessage "Hello, World!"

printMessage :: String -> IO ()
printMessage = putStrLn
