from utils.run_sql_command import run_sql_command
from prettytable import PrettyTable


def buyin_report(database_file_path: str) -> PrettyTable:

    query = '''
    WITH 
    
    didCash AS (
        SELECT
            price as pc1,
            prize,
            COUNT(*) as count
        FROM
            tournaments
        WHERE
            prize>0
        GROUP BY 
            pc1),
        
    totalNB AS (
        SELECT
            price as pc2,
            sum(prize) as prizes,
            sum(price) as prices,
            COUNT(*) as count
        FROM
            tournaments
        GROUP BY
            pc2),
    
    avgProfitPerGame AS (
        SELECT 
            price as pc3,
            round((avg(prize/price)*price)-price, 2) as avgProfit
        FROM 
            tournaments
        GROUP BY 
            price)
    
    SELECT
        pc1,
        ROUND((totalNB.count * 1.0 / didCash.count) * 10, 1),
        ROUND(totalNB.prizes, 2),
        ROUND(totalNB.prices, 2),
        ROUND(totalNB.prizes-totalNB.prices),
        totalNB.count,
        avgProfitPerGame.avgProfit
    FROM
        didCash
        
    INNER JOIN totalNB
    ON didCash.pc1 = totalNB.pc2
    
    INNER JOIN avgProfitPerGame
    ON avgProfitPerGame.pc3 = totalNB.pc2
    '''

    data = run_sql_command(
        query=query,
        unique_items=False,
        database_file_path=database_file_path)

    t = PrettyTable(['Buyin', 'ITM %', 'Net', 'Invested', 'Profit', 'Count', 'Avg. profit/game'])

    for buyin, itm, totalPrizes, totalPrices, count, profit, avgProfitPerGame in data:
        t.add_row([buyin, itm, totalPrizes, totalPrices, count, profit, avgProfitPerGame])

    return t
